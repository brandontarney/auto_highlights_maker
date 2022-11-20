# auto_movie_maker
Automatically create a movie (and upload it)

## Background:
When playing modern PC video games highlight videos are captured for certain in-game events automatically. This leaves the user with the **problem** of deciphering which videos are worth sharing and *actually sharing* the videos in a concise manor. In the past this meant the user would review all videos, select the best videos, combine the videos into one video manually with a video editor, and upload the video manually to youtube or a similar website. Not only is this a manually intensive task, but the output product is less than ideal since overlapping highlight videos require manual trimming or otherwise have duplicate frames in the final single video (the video has overlapping/repeated sections). 

This project seeks to automate and improve the before-mentioned process. 
1. Find the best videos automatically
2. Combine the videos automatically (and skip overlapping/repeated frames!)
3. Upload the final single video to youtube

## How-To Run:
1. Setup python environment via requirements.txt
    - recommendation: 
        - `python -m venv venv`
        - `source venv/Scripts/activate`
        - `pip install -r requirements.txt`
2. Collect relevant times of highlight videos captured via `record_date_time*` script after every in-game highlight
    - I recommend using the `*.exe` program in your Windows taskbar so you can quickly run the script while playing a game
3. Run `auto_movie_maker_PLATFORM.sh` to:
    1. Find matching highlight files for previously manually recorded times (see previous step)
        - `find_close_files_by_time.py` to find the correct highlight videos
    2. Concatenate all relevant clips (and remove duplicate frames) into a single movie
        - `clip-cat/main.py` to concatenate the videos you want to upload into a single video without overlapping frames
    3. Upload the movie (scripts exist for Youtube and Vimeo, but Vimeo is the currently chosen upload)
        - `upload.py` to upload the video to youtube
    	      - Note this will require Youtube API or Vimeo API stuff (see here: [youtube-api](https://simple-youtube-api.readthedocs.io/install.html) and here: [how-to-make-yt-uploads-public](https://stackoverflow.com/questions/64079139/using-youtube-data-api-makes-my-videos-private-on-upload/64080239#64080239) or here: [vimeo API help](https://developer.vimeo.com/api/guides/start))


