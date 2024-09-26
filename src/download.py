import requests

def get_download_links(session_cookie, request_id):
    url = f'https://api.deepmotion.com/download/{request_id}'
    headers = {
        'cookie': f'dmsess={session_cookie}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()['urls']
    else:
        raise Exception(f"Failed to get download links: {response.status_code}, {response.text}")

def download_file(download_url, output_path):
    response = requests.get(download_url)

    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully: {output_path}")
    else:
        raise Exception(f"Failed to download file: {response.status_code}, {response.text}")
