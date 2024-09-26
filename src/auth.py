import requests
import base64

def get_session_cookie(client_id, client_secret):
    auth_str = f"{client_id}:{client_secret}"
    auth_bytes = auth_str.encode('ascii')
    auth_base64 = base64.b64encode(auth_bytes).decode('ascii')

    headers = {
        'Authorization': f'Basic {auth_base64}'
    }

    url = 'https://api.deepmotion.com/session/auth'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.cookies['dmsess']
    else:
        raise Exception(f"Failed to get session cookie: {response.status_code}, {response.text}")
