import os
import requests

url = "https://hapi.fhir.org/baseR4/Appointment"
params = {"status": "cancelled", "_count": 50}

response = requests.get(url, params=params)
data = response.json()

appointments = data.get("entry", [])
print(f"Found {len(appointments)} cancelled appointments")

webhook = os.environ["SLACK_WEBHOOK_URL"]
message = {"text": f"Appointment alert: {len(appointments)} cancelled appointments found."}
requests.post(webhook, json=message)
print("Sent to Slack")

