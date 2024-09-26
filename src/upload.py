import requests

def get_upload_url(session_cookie, filename):
    url = 'https://api.deepmotion.com/upload'
    headers = {
        'cookie': f'dmsess={session_cookie}'
    }
    params = {
        'name': filename,
        'resumable': '1'
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()['url']
    else:
        raise Exception(f"Failed to get upload URL: {response.status_code}, {response.text}")

def upload_video(upload_url, file_path):
    with open(file_path, 'rb') as video_file:
        video_data = video_file.read()

    response = requests.put(upload_url, data=video_data)

    if response.status_code == 200:
        print("Video uploaded successfully")
    else:
        raise Exception(f"Failed to upload video: {response.status_code}, {response.text}")
