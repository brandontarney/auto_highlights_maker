# TODO: Upload to youtube?
# TODO: Seems like all videos are locked private...
    #- https://support.google.com/youtube/contact/yt_api_form
    # - https://drjohnstechtalk.com/blog/2021/10/automated-youtube-video-uploading-from-raspberry-pi-without-using-youtube-api/
    # Alternative via selenium? https://pypi.org/project/youtube-uploader-selenium/
# Another option: https://github.com/tokland/youtube-upload
# Another option: Vimeo!? https://developer.vimeo.com/api/guides/videos/upload


# Libraries:
# pip install simple-youtube-api

from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo

# loggin into the channel
channel = Channel()
#channel.login("client_secret.json", "credentials.storage")
channel.login("/Users/brandontarney/Dropbox/3_save/client_secret.json", "credentials.storage")

# setting up the video that is going to be uploaded
video = LocalVideo(file_path="test_videos/output.mp4")

# setting snippet
video.set_title("315Highlights")
video.set_description("Fortnite Hightlights")
#video.set_tags(["this", "tag"])
#video.set_category("gaming")
video.set_default_language("en-US")

# setting status
video.set_made_for_kids(False)
video.set_embeddable(True)
video.set_license("creativeCommon")
#video.set_privacy_status("private")
video.set_privacy_status("unlisted")
#video.set_public_stats_viewable(True)

# setting thumbnail
#video.set_thumbnail_path('test_thumb.png')

# uploading video and printing the results
video = channel.upload_video(video)
print("https://youtu.be/" + video.id)
#print(video)

# liking video
#video.like()
