#!/bin/sh
create_ffmpeg_concat_file.bash
ffmpeg -f concat -safe 0 -i VideoFileList.txt -c copy output.mp4
