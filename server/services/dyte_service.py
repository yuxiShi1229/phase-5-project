import requests
import base64
import os

DYTE_BASE_URL = "https://api.dyte.io/v2"
DYTE_ORG_ID = os.environ.get("DYTE_ORG_ID")
DYTE_API_KEY = os.environ.get("DYTE_API_KEY")

def get_auth_header():
    credentials = f"{DYTE_ORG_ID}:{DYTE_API_KEY}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    return f"Basic {encoded_credentials}"

def create_dyte_meeting(classroom_id):
    url = f"{DYTE_BASE_URL}/meetings"
    headers = {
        "Authorization": get_auth_header(),
        "Content-Type": "application/json"
    }
    data = {
        "title": f"Classroom {classroom_id}",
        "preferred_region": "ap-south-1",
        "record_on_start": False
    }
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()["data"]["id"]

def create_dyte_participant_token(meeting_id, user_id, username):
    url = f"{DYTE_BASE_URL}/meetings/{meeting_id}/participants"
    headers = {
        "Authorization": get_auth_header(),
        "Content-Type": "application/json"
    }
    data = {
        "client_specific_id": str(user_id),
        "name": username,
        "preset_name": "group_call_participant"
    }
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()["data"]["token"]