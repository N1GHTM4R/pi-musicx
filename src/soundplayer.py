from playsound import playsound # type: ignore #NOTE: This just ignores the error here, its really annoying lol.
import os

def play_sound(file_name):
    # * Get the absolute path to the sound file
    sound_file_path = os.path.abspath(file_name)

    # * Print the absolute path to verify it
    print(f"Sound file path: {sound_file_path}")

    # * Check if the file exists
    if os.path.exists(sound_file_path):
        print("File exists, playing sound...")
        # * Play the sound file
        playsound(sound_file_path)
    else:
        # ! Error: Handle the case where the file does not exist
        print("File does not exist at the specified path.")