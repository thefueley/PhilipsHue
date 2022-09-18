import os
import requests
import time
import urllib3
from flask import Flask

HUE_API = os.environ['HUE_API']
HUE_API_KEY = os.environ['HUE_API_KEY']

app = Flask(__name__)

@app.route('/')
def toggleBlueRoom():
    urllib3.disable_warnings()
    if HUE_API_KEY is None:
        return "HUE_API value not set!"
    if HUE_API is None:
        return "HUE_API_KEY not set!"

    headers={'hue-application-key': HUE_API_KEY, "Cache-Control": "no-cache"}

    # Blue Room Lights Status
    location_endpoint = f"{HUE_API}/grouped_light/3ce6a6c4-38c1-448a-bddd-08182fb53918"
    r = requests.get(url=location_endpoint, headers=headers, verify=False)
    data = r.json()
    current_status = data['data'][0]['on']
    print(f"Current Status: {current_status}")

    time.sleep(1)

    if (current_status.get('on') == True):
        print("Turning off BlueRoom lights")
        r = requests.put(url=location_endpoint, headers=headers, json={"on": {"on":False}}, verify=False)
        if r.status_code == 207:
            return f"{r.reason}"
        else:
            return f"Status: {r.status_code}"
    else:
        print("Turning on BlueRoom lights")
        r = requests.put(url=location_endpoint, headers=headers, json={"on": {"on":True}}, verify=False)
        if r.status_code == 207:
            print(r.json())
            return f"{r.reason}"
        else:
            return f"Status: {r.status_code}"
