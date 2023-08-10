import requests

repository_url = "https://your.repository.url"
username = "your_username"
password = "your_password"

try:
    response = requests.get(repository_url, auth=(username, password))
    if response.status_code == 200:
        print("Connection to Nexus repository successful!")
    else:
        print(f"Connection to Nexus repository failed with status code: {response.status_code}")
except requests.RequestException as e:
    print(f"Connection to Nexus repository failed: {e}")