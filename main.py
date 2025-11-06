import os
import shutil

# Ask the user for the folder to organize
folder_to_organize = input("Enter the full path of the folder you want to organize: ").strip()

# Check if folder exists
if not os.path.isdir(folder_to_organize):
    print("!!!! The folder does not exist. Please check the path and try again. !!!!")
    exit()

organized_folder = os.path.join(folder_to_organize, "Organized")

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

# Create category folders
for category in categories:
    folder_path = os.path.join(organized_folder, category)
    os.makedirs(folder_path, exist_ok=True)

# Move files into categories
for file_name in os.listdir(folder_to_organize):
    file_path = os.path.join(folder_to_organize, file_name)
    
    # Skip folders
    if not os.path.isfile(file_path):
        continue
    
    moved = False
    for category, extensions in categories.items():
        if file_name.lower().endswith(tuple(extensions)):
            shutil.move(file_path, os.path.join(organized_folder, category, file_name))
            moved = True
            break
    
    # Move uncategorized files to Misc
    if not moved:
        misc_folder = os.path.join(organized_folder, "Misc")
        shutil.move(file_path, os.path.join(misc_folder, file_name))

print("Folder organized successfully!")
