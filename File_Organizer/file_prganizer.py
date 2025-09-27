import os, shutil

# folder to organize
source = "C:/Users/YourName/Desktop/OrganizerTest"

# mapping
mapping = {
    "Images": [".jpg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3"],
    "Videos": [".mp4", ".mkv"]
}

for file in os.listdir(source):
    file_path = os.path.join(source, file)
    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()
        for folder, extensions in mapping.items():
            if ext in extensions:
                folder_path = os.path.join(source, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file))
                break
