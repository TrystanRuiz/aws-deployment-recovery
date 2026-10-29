import argparse
import json
from urllib.request import urlopen

parser = argparse.ArgumentParser(description="Verify application health and version")
parser.add_argument("--expected-version", required=True)
parser.add_argument("--url", default="http://127.0.0.1:8000/health")
args = parser.parse_args()

with urlopen(args.url, timeout=5) as response:
    result = json.load(response)

expected_version = args.expected_version

if result.get("status") == "healthy" and result.get("version") == expected_version:
    print(f"PASS: healthy version {expected_version}")
    raise SystemExit(0)
else:
    print(f"FAIL: expected healthy version {expected_version}, received {result}")
    raise SystemExit(1)