from pathlib import Path
import hashlib

src = Path("internal.cpp")
mp3 = Path("assets/teeth.mp3")
out = Path("output/teeth.mp3")
marker = b"\nMP3SOURCE-TEST-V1\n"

if not src.is_file():
    raise SystemExit("internal.cpp missing")
if not mp3.is_file():
    raise SystemExit("assets/teeth.mp3 missing")

source = src.read_bytes()
data = mp3.read_bytes() + marker + source
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(data)

print(f"created {out} ({out.stat().st_size} bytes)")
print("embedded internal.cpp SHA256:", hashlib.sha256(source).hexdigest())
