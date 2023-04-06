import boto3
from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import StreamingResponse
from typing import List
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# Create an S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION_NAME')
)

app = FastAPI()

@app.post("/upload/")
async def upload_video(video_file: UploadFile = File(...)):
    # Upload the video file to S3
    s3.upload_fileobj(video_file.file, os.getenv('AWS_BUCKET_NAME'), video_file.filename)
    return {"filename": video_file.filename}

@app.get("/stream/{filename}")
async def stream_video(filename: str):
    # Stream the video from S3
    try:
        response = s3.get_object(Bucket=os.getenv('AWS_BUCKET_NAME'), Key=filename)
        video_bytes = response["Body"].read()
        return StreamingResponse(video_bytes, media_type="video/mp4")
    except s3.exceptions.NoSuchKey:
        return Response(status_code=404)

@app.get("/download/{filename}")
async def download_video(filename: str):
    # Download the video from S3
    try:
        response = s3.get_object(Bucket=os.getenv('AWS_BUCKET_NAME'), Key=filename)
        video_bytes = response["Body"].read()
        return Response(content=video_bytes, media_type="video/mp4", headers={"Content-Disposition": f"attachment; filename={filename}"})
    except s3.exceptions.NoSuchKey:
        return Response(status_code=404)

@app.get("/list/")
async def list_videos():
    # List all videos in the S3 bucket
    response = s3.list_objects_v2(Bucket=os.getenv('AWS_BUCKET_NAME'))
    videos = [obj["Key"] for obj in response.get("Contents", [])]
    return {"videos": videos}
