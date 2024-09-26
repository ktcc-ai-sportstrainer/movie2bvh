import time
from auth import get_session_cookie
from upload import get_upload_url, upload_video
from process import start_processing, check_status
from download import get_download_links, download_file

def main():
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    video_path = '../data/test.mp4'
    output_bvh_path = '../data/output.bvh'
    
    try:
        # 認証してセッションクッキーを取得
        session_cookie = get_session_cookie(client_id, client_secret)
        print("Session cookie obtained.")

        # アップ
            # アップロードURLを取得
        upload_url = get_upload_url(session_cookie, 'test.mp4')
        print("Upload URL obtained.")

        # 動画をアップロード
        upload_video(upload_url, video_path)
        print("Video uploaded successfully.")

        # 動画処理を開始
        request_id = start_processing(session_cookie, upload_url)
        print(f"Processing started, request ID: {request_id}")

        # 処理が完了するまでステータスをチェック
        print("Waiting for processing to complete...")
        while True:
            status = check_status(session_cookie, request_id)
            if status['status'][0]['status'] == 'SUCCESS':
                print("Processing completed successfully.")
                break
            elif status['status'][0]['status'] == 'FAILURE':
                raise Exception("Processing failed.")
            else:
                print(f"Processing status: {status['status'][0]['status']}")
                time.sleep(10)  # 10秒待機して再チェック

        # ダウンロードリンクを取得
        download_links = get_download_links(session_cookie, request_id)
        bvh_url = None
        for link in download_links:
            for file_type, file_url in link['files'].items():
                if file_type == 'bvh':
                    bvh_url = file_url
                    break

        if bvh_url:
            # BVHファイルをダウンロード
            download_file(bvh_url, output_bvh_path)
            print(f"BVH file downloaded to {output_bvh_path}")
        else:
            raise Exception("BVH file not found in download links.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

