# AI_Disk_Cleanup_Recommender
AI-powered disk cleanup recommendation system that analyzes files and folders, identifies unnecessary storage usage, and suggests safe cleanup actions through an interactive Streamlit dashboard.
# AI Disk Cleanup Recommender

## Overview

AI Disk Cleanup Recommender is a Python-based application that helps users analyze disk usage and identify files that may be consuming unnecessary storage space. The application scans directories, categorizes files, and provides intelligent recommendations for cleanup through an interactive Streamlit dashboard.

The goal of this project is to assist users in maintaining a clean and efficient system by highlighting temporary files, log files, large files, and other storage-heavy content that can be safely reviewed for deletion.

---

## Features

* Scan selected folders and directories
* Detect large files consuming excessive disk space
* Identify temporary files
* Detect log files
* Generate cleanup recommendations
* Interactive Streamlit-based dashboard
* Easy-to-understand storage analysis
* User-friendly interface

---

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* OS Module
* Pathlib

---

## Project Structure

```text
AI_Disk_Cleanup_Recommender/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
├── logs/
└── assets/
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/AI_Disk_Cleanup_Recommender.git
cd AI_Disk_Cleanup_Recommender
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will automatically open in your default browser.

---

## How It Works

1. Select a directory to analyze.
2. The application scans files and folders.
3. File sizes and categories are evaluated.
4. Cleanup recommendations are generated.
5. Users can review suggested files before taking any action.

---

## Use Cases

* Free up disk space
* Identify unnecessary files
* Monitor storage consumption
* Improve system organization
* Support regular maintenance activities

---

## Future Enhancements

* Duplicate file detection
* AI-based cleanup scoring
* File age analysis
* Automated cleanup suggestions
* Export reports to PDF
* Scheduled scans

---

## Author

**B. S. N. V. Satyanarayana**

Software Developer | Trainer | Author

---

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and professional purposes.
