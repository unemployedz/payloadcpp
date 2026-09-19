from pathlib import Path
import hashlib

src = Path("output/payload_test")
mp3 = Path("assets/teeth.mp3")
out = Path("output/teeth.mp3")
marker = b"\nMP3PAYLOAD-TEST-V1\n"

if not src.is_file():
    raise SystemExit("compiled test program missing")
if not mp3.is_file():
    raise SystemExit("assets/teeth.mp3 missing")

data = mp3.read_bytes() + marker + src.read_bytes()
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(data)
print(f"created {out} ({out.stat().st_size} bytes)")
print("embedded test SHA256:", hashlib.sha256(src.read_bytes()).hexdigest())
