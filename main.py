import sys
from json import loads as json
from base64 import b64decode as base64
import requests
from requests.structures import CaseInsensitiveDict
import config

args = sys.argv[1:]
if(len(args) < 3 or len(args) > 3):
    print("Usage: python main.py [USERNAME] [REPOSITORY] [FILEPATH]")
    exit(1)

url = f"https://api.github.com/repos/{args[0]}/{args[1]}/contents/{args[2]}"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {config.token}"
headers["Method"] = "GET"

resp = ""
print(f"Attempting to resolve: {url}")
try:
    resp = requests.get(url, headers=headers)
    print(resp.status_code)
except Exception as e:
    print(f"Error with request.\n{e}")

print(str(base64(resp.json()["content"])).replace("\\n", "\n"))