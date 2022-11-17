# Using Selenium, e.g. the UI, upload a video to youtube
from youtube_uploader_selenium import YouTubeUploader

video_path = 'test_videos/output.mp4'

uploader = YouTubeUploader(video_path)
was_video_uploaded, video_id = uploader.upload()
assert was_video_uploaded
