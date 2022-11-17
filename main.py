# Script to run entire auto-movie-maker pipeline...
# - Get appropriate videos
# - Concatenate videos
# - Upload videos
import fire
from find_close_files_by_time import find_close_files_by_time
import importlib
clip_cat = importlib.import_module("clip-cat.main")
from upload import upload_vimeo_api


def make_movie(fortnite_clip_search_limit_in_seconds,
               token_file_path, client_id_file_path, client_secret_file_path,
               fortnite_video_directory_path="test_videos/",
               manual_date_time_file_path="test_videos/date_list.txt",
               videos_selected_for_upload_path="test_videos/selected_files_list.txt",
               upload_directory_path="test_videos/uploads/",
               upload_video_name="upload",
               upload_video_description="video uploaded from auto_movie_maker"):

    print("\n- START: Finding video files to concatenate via find_close_files_by_time.py")
    find_close_files_by_time.find_close_files_by_time( fortnite_clip_search_limit_in_seconds,
                             fortnite_video_directory_path,
                             manual_date_time_file_path,
                             videos_selected_for_upload_path,
                             upload_directory_path )
    print("- END: Finding video files to concatenate via find_close_files_by_time.py\n")

    print("\n- START: concatenating videos")
    clip_cat.create(upload_directory_path)
    print("- END: concatenating videos\n")

    concatenated_video_for_upload = upload_directory_path + "/concatenation.mp4"

    print("\n- START: uploading video")
    upload_vimeo_api.upload_video(token_file_path, client_id_file_path, client_secret_file_path, 
                                  concatenated_video_for_upload, upload_video_name, upload_video_description)
    print("- END: uploading video\n")

    
if __name__ == "__main__":
    print("\n- START: AUTO_MOVIE_MAKER")
    fire.Fire(make_movie)
    print("- END: AUTO_MOVIE_MAKER\n")
