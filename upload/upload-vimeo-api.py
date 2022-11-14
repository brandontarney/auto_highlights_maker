# Upload video to vimeo
# https://developer.vimeo.com/api/guides/videos/upload
import vimeo
import fire

# UPLOAD_VIDEO: method to upload video to vimeo
def upload_video(token_file_path, client_id_file_path, client_secret_file_path, video_file_path, video_name='upload', video_description='video uplaoded from auto_movie_maker'):
    with open(token_file_path, 'r') as token_file:
        token = token_file.read().replace('\n','')
        print("Token: " + token)
    with open(client_id_file_path, 'r') as client_id_file:
        client_id = client_id_file.read().replace('\n','')
        print("Client_ID: " + client_id)
    with open(client_secret_file_path, 'r') as client_seecret_file:
        client_secret = client_seecret_file.read().replace('\n','')
        print("Client_server: " + client_secret)

    client = vimeo.VimeoClient( token=token, key=client_id, secret=client_secret)
    uri = client.upload(video_file_path, data={ 'name':video_name, 'description':video_description})

    response = client.get(uri + '?fields=transcode.status').json()
    if response['transcode']['status'] == 'complete':
        print('Your video finished transcoding.')
    elif response['transcode']['status'] == 'in_progress':
        print('Your video is still transcoding.')
    else:
        print('Your video encountered an error during transcoding.')
    
    response = client.get(uri + '?fields=link').json()
    print("Your video link is: " + response['link'])


if __name__ == '__main__':
  fire.Fire(upload_video)

