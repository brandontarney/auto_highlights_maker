from datetime import datetime
import os
import shutil
import fire


# TODO: Default paths here are easy to break if you don't run this script from within the base directory
def find_close_files_by_time( fortnite_clip_search_limit_in_seconds,
                             fortnite_video_directory_path="test_videos/",
                             manual_date_time_file_path="test_videos/date_list.txt",
                             selected_files_file_path="test_videos/selected_files_list.txt",
                             upload_directory_path="test_videos/uploads/" ):

    print(f"- INPUT: fortnite_clip_search_limit(s): {fortnite_clip_search_limit_in_seconds}")
    print(f"- INPUT: fortnite highlights found here: {fortnite_video_directory_path}")
    print(f"- INPUT: manual date/times found here: {manual_date_time_file_path}")

    manual_date_time_format = "%y.%m.%d - %H.%M.%S"
    fortnite_highlight_date_time_format = "%Y.%m.%d - %H.%M.%S"

    # List the directories in the Fortnite folder && date_list file
    all_files = os.listdir(fortnite_video_directory_path)
    fortnite_highlight_files = [files.strip() for files in all_files if files.rfind("DVR") >= 0]
    print(f"- PROCESSING: fortnite_highlight_files: {fortnite_highlight_files}")
    with open(manual_date_time_file_path) as file:
        manual_date_times = [datetime.strptime(line.strip(), manual_date_time_format) for line in file if line]
        print(f"- PROCESSING: manual_date_times: {manual_date_times}")

    # Convert to date/time && map times to filenames
    fortnite_highlight_date_to_file_map = \
        dict([ (datetime.strptime( \
            fortnite_file.replace(".DVR", "").replace("Fortnite ", "").replace(".mp4","")[:-3], \
            fortnite_highlight_date_time_format),fortnite_file) for fortnite_file in fortnite_highlight_files ])
    print(f"- PROCESSING: fortnite_highlight_date_to_file_map: {fortnite_highlight_date_to_file_map}")

    # Get files that have "close" times to date_list file
    fortnite_highlights_chosen_for_manual_date_times = {} #{manual_date:fortnite_date_list}
    for manual_date_time in manual_date_times:
        for fortnite_file_date_time, fortnite_file in fortnite_highlight_date_to_file_map.items():
            absolute_time_diff_in_seconds = abs((manual_date_time - fortnite_file_date_time).total_seconds())
            #print(f"time_diff: {absolute_time_diff_in_seconds}")
            if 0 < absolute_time_diff_in_seconds < fortnite_clip_search_limit_in_seconds:
                #print(f"FOUND A CLIP: {fortnite_file}")
                if manual_date_time in fortnite_highlights_chosen_for_manual_date_times:
                    fortnite_highlights_chosen_for_manual_date_times[manual_date_time].append(fortnite_file)
                else:
                    fortnite_highlights_chosen_for_manual_date_times[manual_date_time] = [fortnite_file]

    print(f"- PROCESSING: fortnite_highlights_chosen_for_manual_date_times: {fortnite_highlights_chosen_for_manual_date_times}")

    print(f"- FINISHING: writing chosen fortnite highlights here: {selected_files_file_path}")
    print(f"- FINISHING: copying chosen fortnite highlights here: {upload_directory_path}")
    # write all clips found to file
    with open(selected_files_file_path, 'w') as selected_files_file:
        for (date, files) in fortnite_highlights_chosen_for_manual_date_times.items():
            #selected_files_file.write('\n'.join(files))
            selected_files_file.write(str(date) + '\n')
            for file in files:
                selected_files_file.write('\t' + file)
                shutil.copyfile(fortnite_video_directory_path + file, upload_directory_path + file)



if __name__ == "__main__":
    print("\n- START: FIND_CLOSE_FILES_BY_TIME")
    fire.Fire(find_close_files_by_time)
    print("- END: FIND_CLOSE_FILES_BY_TIME\n")

