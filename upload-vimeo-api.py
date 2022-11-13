# Upload video to vimeo
# https://developer.vimeo.com/api/guides/start
# https://developer.vimeo.com/api/guides/videos/upload
import vimeo

  client = vimeo.VimeoClient(
    token='{access_token}',
    key='{client_id}',
    secret='{client_secret}'
  )

  response = client.get(uri)
  print(response.json())
