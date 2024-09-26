import requests

def start_processing(session_cookie, upload_url):
    url = 'https://api.deepmotion.com/process'
    headers = {
        'cookie': f'dmsess={session_cookie}',
        'Content-Type': 'application/json'
    }
    json_body = {
        'url': upload_url,
        'processor': 'video2anim',
        'params': [
            "formats=bvh,fbx,mp4",  # 必要なフォーマット
            "sim=1"                 # 物理シミュレーションを有効
        ]
    }

    response = requests.post(url, headers=headers, json=json_body)

    if response.status_code == 200:
        return response.json()['rid']
    else:
        raise Exception(f"Failed to start processing: {response.status_code}, {response.text}")

def check_status(session_cookie, request_id):
    url = f'https://api.deepmotion.com/status/{request_id}'
    headers = {
        'cookie': f'dmsess={session_cookie}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to check status: {response.status_code}, {response.text}")
