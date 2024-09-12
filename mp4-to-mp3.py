import os
import ffmpeg

def convert_mp4_to_mp3(input_file, output_folder):
    try:
        # Get the base name (filename without extension) from input file
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        
        # Construct the output file path with .mp3 extension
        output_file = os.path.join(output_folder, base_name + ".mp3")
        
        # Run ffmpeg to convert the MP4 file to MP3
        (
            ffmpeg
            .input(input_file)
            .output(output_file, format='mp3')
            .run(overwrite_output=True)
        )
        
        print(f"File successfully converted to {output_file}")
    except ffmpeg.Error as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Provide input file path and output folder path
    input_file = input("Enter the input MP4 file path: ")
    output_folder = input("Enter the output folder path: ")
    
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        print(f"Output folder {output_folder} does not exist.")
    else:
        convert_mp4_to_mp3(input_file, output_folder)
