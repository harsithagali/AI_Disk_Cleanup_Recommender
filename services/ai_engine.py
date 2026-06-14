def classify_files(files):
    delete_list = []
    keep_list = []
    review_list = []

    for file in files:
        name = file["name"].lower()
        size = file["size"]

        if any(keyword in name for keyword in ["temp", "log", "cache"]):
            delete_list.append(file)

        elif any(keyword in name for keyword in ["report", "notes"]):
            keep_list.append(file)

        elif size > 50:
            review_list.append(file)

        else:
            keep_list.append(file)

    return delete_list, keep_list, review_list