import os
import shutil

home_directory = os.path.expanduser('~')
directory = os.path.join(home_directory, "OneDrive/Desktop/Python Project/Test Folder")
destination = directory


file_extensions = {
    "jpg": "IMAGES",
    "png": "IMAGES",
    "ico": "IMAGES",
    "gif": "IMAGES",
    "svg": "IMAGES",
    "exe": "APP",
    "msi": "APP",
    "pdf": "PDF",
    "xlsx": "EXCEL",
    "csv": "EXCEL",
    "rar": "EXCEL",
    "zip": "ARCHIVE",
    "gz": "ARCHIVE",
    "tar": "ARCHIVE",
    "docx": "WORD",
    "torrent": "TORRENT",
    "txt": "TEXT",
    "ipynb": "PYTHON",
    "py": "PYTHON",
    "pptx": "POWERPOINT",
    "ppt": "POWERPOINT",
    "mp3": "AUDIO",
    "wav": "AUDIO",
    "mp4": "VIDEO",
    "m3u8": "VIDEO",
    "webm": "VIDEO",
    "ts": "VIDEO",
    "css": "WEB",
    "js": "WEB",
    "html": "WEB",
}

file_extensions = {ext.lower(): category for ext, category in file_extensions.items()}

required_folders = set(file_extensions.values())
for folder in required_folders:
    os.makedirs(os.path.join(directory, folder))
    print(f"Folder {folder} is ready!")

source_path = os.listdir(directory)
for file in source_path:
    file_lower = file.lower()
    file_extension = file_lower.split('.')[-1]
    if file_extension in file_extensions:
        target_folder = file_extensions[file_extension]
        target_path = os.path.join(destination, target_folder)
        try:
            shutil.move(os.path.join(directory, file), os.path.join(target_path, file))
            print(f"Moved {file} to {target_folder} successfully")
        except Exception as e:
            print(f"Failed to move {file}: {e}")
