import streamlit as st
import os

from services.scanner import scan_files
from services.ai_engine import classify_files
from services.cleaner import delete_files
from services.db import init_db, insert_log

# Initialize DB
init_db()

st.title("🧠 AI Disk Cleanup Recommender")

# Input
folder_path = st.text_input("Enter Folder Path", "data/sample_files")

if not os.path.exists(folder_path):
    st.error("Invalid folder path")
    st.stop()

# Session state
if "files" not in st.session_state:
    st.session_state.files = []

if "classified" not in st.session_state:
    st.session_state.classified = None

# Scan Button
if st.button("📂 Scan Files"):
    st.session_state.files = scan_files(folder_path)
    st.success(f"{len(st.session_state.files)} files scanned")

# AI Analysis
if st.button("🤖 Run AI Analysis"):
    if st.session_state.files:
        delete_list, keep_list, review_list = classify_files(st.session_state.files)
        st.session_state.classified = (delete_list, keep_list, review_list)
    else:
        st.warning("Scan files first")

# Display Results
if st.session_state.classified:
    delete_list, keep_list, review_list = st.session_state.classified

    st.subheader("📊 Summary")

    st.write(f"Total Files: {len(st.session_state.files)}")

    # DELETE
    st.subheader("🗑️ Files to Delete")
    for f in delete_list:
        st.write(f"{f['name']} ({f['size']} MB)")

    # KEEP
    st.subheader("✅ Files to Keep")
    for f in keep_list:
        st.write(f"{f['name']} ({f['size']} MB)")

    # REVIEW
    st.subheader("⚠️ Files for Review")
    for f in review_list:
        st.write(f"{f['name']} ({f['size']} MB)")

# Cleanup Button
if st.button("🚀 Approve Cleanup"):
    if st.session_state.classified:
        delete_list, keep_list, review_list = st.session_state.classified

        deleted_files, space = delete_files(delete_list)

        st.success("Cleanup Completed")

        st.write("### Deleted Files")
        for f in deleted_files:
            st.write(f)

        st.write(f"### Space Recovered: {space} MB")

        # Save log
        insert_log(
            scanned=len(st.session_state.files),
            deleted=len(delete_list),
            kept=len(keep_list),
            space=space
        )

    else:
        st.warning("Run analysis first")