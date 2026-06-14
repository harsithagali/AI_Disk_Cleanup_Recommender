import os

def scan_files(folder_path):
    file_data = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            size_mb = os.path.getsize(full_path) / (1024 * 1024)

            file_data.append({
                "name": file,
                "path": full_path,
                "size": round(size_mb, 2)
            })

    return file_data