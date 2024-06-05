import os
import re

# Loop through all directories in the current directory
for folder_name in next(os.walk('.'))[1]:
    # Define the show name based on the folder name
    show_name = folder_name
    # Construct the path to the folder
    folder_path = os.path.join('.', folder_name)
    
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Use regular expression to find the episode number
        # This regex now looks for 'Episode XX', 'Ep XX', or 'SXX EXX'
        match = re.search(r'(?:Episode|Ep|\bS\d{2}\sE)\s?(\d+)', filename, re.IGNORECASE)
        if match:
            # Extract the episode number
            episode_number = match.group(1)
            # Extract the file extension
            extension = filename.split('.')[-1]
            # Construct the new filename in Plex format
            new_filename = f"{show_name} - S01E{episode_number.zfill(2)}.{extension}"
            # Construct the full old and new file paths
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed "{filename}" to "{new_filename}"')

print("Renaming complete.")
