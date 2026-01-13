import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python website_check.py <URL>")
    sys.exit(1)

url = sys.argv[1]
try:
    r = requests.get(url)
    if r.status_code == 200:
        print(f"{url} is working.")
    else:
        print(f"{url} returned status {r.status_code}")
except:
    print(f"Could not connect to {url}")