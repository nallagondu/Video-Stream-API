# Video-Stream-API
This project is a RESTful API for uploading, streaming, and downloading videos. The API is built using FastAPI and stores the videos in Amazon S3.

## Requirements
Python 3.8 or higher
AWS account with S3 permissions

## Getting Started
1. Clone the repository:

`git clone https://github.com/your-username/Video-Stream-API.git`
  
2. Navigate to the project directory:

  `cd video-storage-api`
  
3. Install the required dependencies:

  `$ pip install -r requirements.txt`
  
4. Set the following environment variables:

  `AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
  AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>
  AWS_REGION_NAME=<your_aws_region_name>
  AWS_BUCKET_NAME=<your_aws_bucket_name>`
  
5. Start the server:

  `uvicorn main:app --host 0.0.0.0 --port 8000`
  
6. Use the API endpoints to upload, stream, and download videos:

  `POST /videos - Upload a video
   GET /videos/{video_id}/stream - Stream a video
   GET /videos/{video_id}/download - Download a video`
   
# API Documentation

## Upload a Video

`POST /videos`

Upload a video to the server. The video file should be sent as a form-data file in the video field.

Request

`Content-Type: multipart/form-data

video=<video-file>`

Response

`HTTP/1.1 201 Created

{
  "id": "d7be78a8-9a7a-4f25-8b47-92c8d65e9446",
  "url": "https://s3.amazonaws.com/my-bucket/videos/d7be78a8-9a7a-4f25-8b47-92c8d65e9446.mp4",
  "created_at": "2023-04-06T12:00:00Z"
}`

## Stream a Video

`GET /videos/{video_id}/stream`

Stream a video from the server. The video is streamed using the Range header to support seeking and resuming.

`Range: bytes=<start>-<end>`

Response

`HTTP/1.1 206 Partial Content

Content-Type: video/mp4
Content-Range: bytes <start>-<end>/<total-size>
Content-Length: <content-length>
Content-Disposition: inline; filename="<video_id>.mp4"
Accept-Ranges: bytes

<video-data>`

## Download a Video

`GET /videos/{video_id}/download`

Download a video from the server. The video is downloaded as a file attachment.

Response

`HTTP/1.1 200 OK

Content-Type: application/octet-stream
Content-Disposition: attachment; filename="<video_id>.mp4"
Content-Length: <content-length>

<video-data>`

## Conclusion

That's it! You now have a fully functional video storage API built using FastAPI and AWS S3. You can use this API to upload, stream, and download videos in a scalable and efficient way. Additionally, I have thought of Dockerizing the application, making it easy to deploy and run on any Docker-compatible environment.

This project can be extended and modified to fit your specific needs, such as adding authentication or implementing additional video processing features.
   
