import requests

url = "https://api.clashroyale.com/v1/players/%23"

api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQ4ZWQ5YmM5LTcxMTYtNDZiYi1iMjE4LTg5MDMzY2RjMzgyZSIsImlhdCI6MTc3MjExMDA2OCwic3ViIjoiZGV2ZWxvcGVyL2U0ZTdlNTYzLWI0YjgtYTQ4Yi0yZGUxLWJmMmEzYzJhZWIxZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI2Mi4yMzEuNzIuMTA3Il0sInR5cGUiOiJjbGllbnQifV19.sfylqa5OFcte50dtWwiOYD6tXc7WSV_vaEw93iZfpXyrGy6GaRempqm_tEXGwuNdQrr7jWKfc4bsb2c2Hlb2Xg"


def get_clash_royale_stats():
    id = input("Enter Clash Royale ID: ")
    final_url = url + id
    headers = {
        "Authorization": f"Bearer {api_token}",
    }

    response = requests.get(final_url, headers=headers)

    if response.status_code == 200:
        print("Succes!")
        return response.json()
    else:
        print(f"Eroare {response.status_code}: {response.text}")

info = get_clash_royale_stats()

print(info["trophies"])