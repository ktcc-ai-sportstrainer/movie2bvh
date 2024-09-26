# Animate 3D Python API Integration

This project demonstrates how to integrate the DeepMotion Animate 3D REST API in Python to process videos, convert them into 3D animations, and download the resulting BVH files.

## Features

- Authenticate with the Animate 3D API using client credentials.
- Upload a video to the API for processing.
- Process the video to generate 3D animations.
- Download the resulting BVH file.

## Project Structure

```bash
/your_project
│── /src
│    ├── __init__.py
│    ├── auth.py           # Handles authentication
│    ├── upload.py         # Handles video upload
│    ├── process.py        # Handles video processing
│    ├── download.py       # Handles file downloads
│    └── main.py           # Main script to run the process
│── /data
│    └── test.mp4          # Video file to be uploaded
│── requirements.txt       # List of required Python packages
```

## Requirements

- Python 3.7 or above
- `requests` library (included in `requirements.txt`)

## Setup Instructions

1. **Clone the repository**

    Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/animate3d-python.git
    cd animate3d-python
    ```

2. **Install required dependencies**

    Install the necessary Python libraries using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Update credentials**

    Open the `src/main.py` file and update the following variables with your **client ID** and **client secret** provided by DeepMotion:

    ```python
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    ```

4. **Add a video file**

    Place the video file you want to process into the `/data` folder. You can rename the file or update the `video_path` in the `src/main.py` file to point to the correct file:

    ```python
    video_path = '../data/test.mp4'
    ```

## Usage

1. **Run the main script**

    Run the `main.py` script from the `src` directory to upload the video, start the processing, and download the resulting BVH file:

    ```bash
    python src/main.py
    ```

2. **Monitor progress**

    The script will print logs to the console as it progresses through each step:
    - It will authenticate and obtain a session cookie.
    - The video will be uploaded.
    - The processing will begin, and the script will check the status periodically.
    - Once the processing is complete, it will download the BVH file to the `/data` directory.

3. **Output**

    The downloaded BVH file will be saved in the `/data` directory with the name `output.bvh`.

## Example Output

```
Session cookie obtained.
Upload URL obtained.
Video uploaded successfully.
Processing started, request ID: 1234567890
Waiting for processing to complete...
Processing status: PROGRESS
Processing status: PROGRESS
Processing completed successfully.
BVH file downloaded to ../data/output.bvh
```

## Troubleshooting

- **Authentication failed**: Ensure your `client_id` and `client_secret` are correct.
- **Video upload failed**: Check if the file path to the video is correct and ensure the file size meets the API requirements.
- **Processing status stuck**: If the processing takes too long, verify that the video meets the API's specifications for supported file formats and resolutions.
- **BVH file not found**: If the BVH file is not found, ensure that the processing parameters include the `bvh` format in the `formats` array.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit pull requests or report issues to improve the project.

---

これで、プロジェクトのセットアップ手順から実行方法までが分かりやすく説明されています。`client_id`と`client_secret`の設定方法や、動画ファイルの準備手順、エラーが発生した場合のトラブルシューティングについても記載しています。