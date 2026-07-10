import requests

# URL to check
URL = "http://127.0.0.1:8080"

try:
    response = requests.get(URL, timeout=5)

    print("=" * 50)
    print("APPLICATION HEALTH CHECK")
    print("=" * 50)

    print(f"URL         : {URL}")
    print(f"Status Code : {response.status_code}")

    if response.status_code == 200:
        print("Application Status : UP")
    else:
        print("Application Status : DOWN")

except requests.exceptions.RequestException as e:
    print("=" * 50)
    print("APPLICATION HEALTH CHECK")
    print("=" * 50)
    print(f"URL : {URL}")
    print("Application Status : DOWN")
    print(f"Error : {e}")