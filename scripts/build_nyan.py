from pathlib import Path
import struct
import zlib

SOURCE = Path("internal.cpp")
INPUT = Path("assets/nyan-cat.jpg")
OUTPUT = Path("output/nyan-cat.jpg")
MARKER = b"INTERNAL-CPP-SOURCE-V1\0"

if not SOURCE.is_file():
    raise SystemExit("internal.cpp missing")
if not INPUT.is_file():
    raise SystemExit("assets/nyan-cat.jpg missing")

source = SOURCE.read_bytes()
jpeg = INPUT.read_bytes()

if not jpeg.startswith(b"\xff\xd8"):
    raise SystemExit("fixture is not a JPEG")

# Store the source as a non-executable JPEG APP15 metadata segment.
payload = MARKER + source
if len(payload) > 65533:
    raise SystemExit("internal.cpp is too large for one JPEG metadata segment")

segment = b"\xff\xef" + struct.pack(">H", len(payload) + 2) + payload

# Insert before the first Start Of Scan marker so the JPEG remains decodable.
sos = jpeg.find(b"\xff\xda")
if sos < 0:
    raise SystemExit("JPEG SOS marker not found")

result = jpeg[:sos] + segment + jpeg[sos:]
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_bytes(result)

print(f"created {OUTPUT} ({OUTPUT.stat().st_size} bytes)")
print("embedded source bytes:", len(source))
