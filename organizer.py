import os
import shutil
file_types = {
    "TextFiles": [".txt", ".docx", ".pdf"],
    "Images": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Others": []  # Files that don’t match any category
}

def organize_folder(folder_path):

    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for file in files:
        file_path = os.path.join(folder_path, file)
        file_ext = os.path.splitext(file)[1]  # Get the file extension
        moved = False
    for category, extensions in file_types.items():
            if file_ext.lower() in extensions:
                # Create category folder if it doesn't exist
                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)

                # Move file to the category folder
                shutil.move(file_path, os.path.join(category_folder, file))
                moved = True
                break
    if not moved:  # If file didn't match any category
            others_folder = os.path.join(folder_path, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, file))

    print("Files organized successfully!")

if __name__ == "__main__":
    folder_path = input("Enter the folder path to organize: ")
    organize_folder(folder_path)
