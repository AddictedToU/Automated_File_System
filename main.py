import os
import shutil

# Ask the user for the folder to organize
folder_to_organize = input("Enter the full path of the folder you want to organize: ").strip()

# Check if folder exists
if not os.path.isdir(folder_to_organize):
    print("!!!! The folder does not exist. Please check the path and try again. !!!!")
    exit()

organized_folder = os.path.join(folder_to_organize, "Organized")
os.makedirs(organized_folder, exist_ok=True)  # Create main folder

# Define extensive categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".odt"],
    "Code": [".py", ".js", ".java", ".cpp", ".c", ".cs", ".html", ".css", ".php", ".rb", ".go", ".rs", ".ts"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".iso"],
    "3D Models": [".fbx", ".obj", ".stl", ".dae", ".blend", ".3ds"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Installers": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"],
    "Ebooks": [".epub", ".mobi", ".azw3", ".pdf"],
    "Spreadsheets": [".csv", ".xls", ".xlsx"],
    "Presentations": [".ppt", ".pptx", ".key"],
    "Vector Graphics": [".ai", ".eps", ".svg"],
    "Databases": [".sql", ".db", ".sqlite", ".mdb"],
    "Misc": []  # For anything uncategorized
}

# Keep track of which folders we create and actually move files into
created_folders = {}

# Move files into categories
for file_name in os.listdir(folder_to_organize):
    file_path = os.path.join(folder_to_organize, file_name)
    
    # Skip folders
    if not os.path.isfile(file_path):
        continue
    
    moved = False
    for category, extensions in categories.items():
        if category != "Misc" and file_name.lower().endswith(tuple(extensions)):
            # Create folder if it doesn't exist yet
            if category not in created_folders:
                folder_path = os.path.join(organized_folder, category)
                os.makedirs(folder_path, exist_ok=True)
                created_folders[category] = folder_path
            shutil.move(file_path, os.path.join(created_folders[category], file_name))
            moved = True
            break
    
    # Move uncategorized files to Misc
    if not moved:
        if "Misc" not in created_folders:
            misc_folder = os.path.join(organized_folder, "Misc")
            os.makedirs(misc_folder, exist_ok=True)
            created_folders["Misc"] = misc_folder
        shutil.move(file_path, os.path.join(created_folders["Misc"], file_name))

# Remove any empty folders just in case (shouldn’t happen but safe)
for folder in os.listdir(organized_folder):
    folder_path = os.path.join(organized_folder, folder)
    if os.path.isdir(folder_path) and not os.listdir(folder_path):
        os.rmdir(folder_path)

print("Folder organized successfully! Only folders with files were created.")
