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
2. Run `record_date_time*` script after every memory highlight 
    - Note run whichever program is applicable to your OS
3. Run `find_close_files_by_time.ipynb` to find the correct highlight videos
4. Run `clip-cat/main.py` to concatenate the videos you want to upload into a single video without overlapping frames
5. Run `upload.py` to upload the video to youtube
    - Note this will require Youtube API stuff (see here: [](https://simple-youtube-api.readthedocs.io/install.html) and here: [](https://stackoverflow.com/questions/64079139/using-youtube-data-api-makes-my-videos-private-on-upload/64080239#64080239))


