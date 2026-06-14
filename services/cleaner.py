import os

def delete_files(files):
    deleted = []
    total_space = 0

    for file in files:
        try:
            os.remove(file["path"])
            deleted.append(file["name"])
            total_space += file["size"]
        except Exception as e:
            print(f"Error deleting {file['name']}: {e}")

    return deleted, round(total_space, 2)