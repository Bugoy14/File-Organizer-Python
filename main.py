import os
import shutil

directory = "C:/Users/<current_user>/OneDrive/Desktop/Test-Folder-Organizer"
source_path = os.listdir(directory)
list_folder = ["PDF", "WORD", "VIDEO", "AUDIO", "APP", "EXCEL", "ARCHIVE", "POWERPOINT", "IMAGES", "WEB"]
destination = "C:/Users/<current_user>/OneDrive/Desktop/Test-Folder-Organizer/"

file_extensions = {
    "jpg": "IMAGES",
    "JPG": "IMAGES",
    "png": "IMAGES",
    "ico": "IMAGES",
    "gif": "IMAGES",
    "svg": "IMAGES",
    "sql": "sql",
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
    "torrent": "torrent",
    "txt": "TEXT",
    "ipynb": "python",
    "py": "python",
    "pptx": "POWERPOINT",
    "ppt": "POWERPOINT",
    "mp3": "AUDIO",
    "wav": "AUDIO",
    "mp4": "VIDEO",
    "m3u8": "VIDEO",
    "webm": "VIDEO",
    "ts": "VIDEO",
    "json": "json",
    "css": "WEB",
    "js": "WEB",
    "html": "WEB",
    "apk": "apk",
    "sqlite3": "sqlite3",
}

for name in list_folder:
    path_new = os.path.join(directory, name)
    try:
        os.makedirs(path_new)
        print(f"Successfully created {name} folder!")
    except OSError:
        print(f"Failed to create {name} folder!")


for extension in file_extensions.keys():
    for file in source_path:
        if file.endswith(extension):
            print(f"{file} matches to {extension}")
            if file_extensions[extension] in list_folder:
                shutil.move(os.path.join(directory, file), (os.path.join(destination+file_extensions[extension], file)))
                print("Moving file success!")
