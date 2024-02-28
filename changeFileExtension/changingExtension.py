import os

# Function to rename files with the ".jfif" extension to ".jpeg"
def rename_files(folder_path):
    jfif_files = [f for f in os.listdir(folder_path) if f.endswith('.jfif')]

    for jfif_file in jfif_files:
        new_filename = os.path.splitext(jfif_file)[0] + '.jpeg'
        new_filename_counter = 1

        # Check if the new filename already exists
        while os.path.exists(os.path.join(folder_path, new_filename)):
            new_filename = os.path.splitext(jfif_file)[0] + f'({new_filename_counter}).jpeg'
            new_filename_counter += 1

        # Rename the file
        os.rename(os.path.join(folder_path, jfif_file), os.path.join(folder_path, new_filename))
        print(f"Renamed '{jfif_file}' to '{new_filename}'")

# Example usage:
folder_path = './'
rename_files(folder_path)
