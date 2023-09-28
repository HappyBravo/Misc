# Import the 'os' module for file system operations
import os

# Import the 'ffmpeg_extract_subclip' function from the MoviePy library
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Define a function 'make_pairs' that takes a list of timestamps as input
def make_pairs(timestamp_list):
    # Initialize an empty list called 'pairs' to store pairs of timestamps
    pairs = []

    # Generate pairs of timestamps from the input list
    # Each pair consists of two consecutive timestamps from the input list
    pairs = [(timestamp_list[i], timestamp_list[i+1]) for i in range(len(timestamp_list)-1)]

    # Return the list of generated pairs
    return pairs

# Define a function 'timeStamp_partName_extract' that extracts time stamps and part names
# from a text file specified by 'file_path'.
def timeStamp_partName_extract(file_path):
    # Initialize empty lists to store time stamps, time stamps in seconds, and part names
    time_stamps = []
    time_stamps_in_sec = []
    part_names = []

    # Open the specified file for reading with UTF-8 encoding
    with open(file_path, "r", encoding="utf-8") as f:
        # Read all lines from the file
        _data = f.readlines()

        # Iterate through each line in the file
        lines = _data
        for line in lines:
            # Split the line into parts using whitespace
            line_part = line.split()
            
            # Extract the time stamp from the first part of the line
            time_stamp = line_part[0]
            time_stamps.append(time_stamp)

            # Join the remaining parts as the part name
            part_name = "_".join(line_part[1:])
            part_names.append(part_name)

            # Split the time stamp into hours, minutes, and seconds
            parts = time_stamp.split(":")
            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = int(parts[2])
            
            # Calculate the total time stamp in seconds
            total_seconds = hours * 3600 + minutes * 60 + seconds
            time_stamps_in_sec.append(total_seconds)
    
    # Return the lists of time stamps in seconds and part names
    return time_stamps_in_sec, part_names

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Define the directory containing the input video
    video_dir = "video"
    
    # Specify the name of the input video file
    video_name = "Bleach_Cour_1_OST.mp4"
    
    # Create the full path to the input video by joining the directory and file name
    video_path = os.path.join(video_dir, video_name)

    # Define the folder where output videos will be saved
    output_video_folder = "video_out"
    
    # Check if the output video folder exists; if not, create it
    if not os.path.exists(output_video_folder):
        os.makedirs(output_video_folder)
    
    # Specify the name of the file containing timestamps
    timestamp_f = "timestamps.txt"

    # Check if the input video file exists
    _exist = os.path.exists(video_path)
    
    if _exist:
        # If the input video exists, set it as the input_video variable
        input_video = video_path
        
        # Call the 'timeStamp_partName_extract' function to extract timestamps and part names
        time_stamps_in_sec, part_names = timeStamp_partName_extract(timestamp_f)
        
        # Generate pairs of start and end timestamps from the extracted timestamps
        cut_ranges = make_pairs(time_stamps_in_sec)

        # Iterate through the cut_ranges and create subclips
        for i, (start, end) in enumerate(cut_ranges):
            # Get the part name for the current segment
            partt = part_names[i]
            
            # Define the output video file name using the original video name and part name
            output_video = f"{video_name[:-4]}__{partt}.mp4"
            
            # Print a message indicating the current operation
            print("Trying... ")
            print(output_video)
            
            # Use 'ffmpeg_extract_subclip' to create a subclip from the input video
            ffmpeg_extract_subclip(input_video, start, end, targetname=os.path.join(output_video_folder, output_video))
            
            # Print a message indicating the completion of the subclip creation
            print(f"--- {output_video} done")

    else:
        # If the input video file doesn't exist, print an error message
        print("video path not correct")

