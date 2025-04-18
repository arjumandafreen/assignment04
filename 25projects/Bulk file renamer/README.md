 🔄 Streamlit Bulk Rename Utility

A simple, elegant web interface (using Streamlit) for batch-renaming files in a directory. This tool preserves the original CLI-based logic and feedback, but transforms it into a user-friendly GUI.

---

## 🚀 Purpose

The purpose of this application is to **bulk rename files** in a selected folder using a predefined renaming rule. Originally built as a command-line interface (CLI) utility, this version modernizes the experience by using **Streamlit** to make it accessible via a web browser without typing commands.

---

## 🧠 Features

- ✅ Rename all files in a folder with a consistent rule
- ✅ Displays success and error messages using visual cues
- ✅ Clean and simple UI (no terminal required)
- ✅ Easily extendable with custom rename logic
- ✅ Built-in error handling and file filtering

---

## 📁 How It Works

### 1. **Directory Input**
The user provides the full path of the folder whose files should be renamed.

```python
directory = st.text_input("📂 Enter the full directory path")
2. Rename Condition
A Python function defines how the filenames should be changed. You can edit this function:

python
Copy
Edit
def rename_condition(filename):
    return 'new_' + filename
✅ Example:
Original file: image1.png
New file: new_image1.png

3. Renaming Process
Once the user clicks the "🚀 Start Renaming" button, the app will:

List all items in the folder

Check if each item is a file (ignores folders)

Rename it using the rename_condition() function

Show success or error messages in the browser

python
Copy
Edit
os.rename(original_path, new_path)
4. Feedback
All progress is shown live in the browser using Streamlit’s message boxes:

✅ Success = st.success()

❌ Error = st.error()

ℹ️ Info = st.info()

⚠️ Warnings = st.warning()

🛠️ How to Use
Step 1: Install Streamlit
bash
Copy
Edit
pip install streamlit
Step 2: Save the Code
Save the following Python code into a file named app.py:

python
Copy
Edit
# Code from app.py (already provided in the previous message)
Step 3: Run the App
In your terminal or command prompt, navigate to the folder where app.py is located, then run:

bash
Copy
Edit
streamlit run app.py
Step 4: Use in Browser
Your browser will open automatically at http://localhost:8501. There, you can:

Enter the full folder path

Click "🚀 Start Renaming"

See results of the renaming process

✏️ Customization
You can modify the renaming logic in the rename_condition() function.

Example 1: Add a prefix
python
Copy
Edit
return 'new_' + filename
Example 2: Replace spaces with dashes
python
Copy
Edit
return filename.replace(" ", "-")
Example 3: Add suffix before extension
python
Copy
Edit
name, ext = os.path.splitext(filename)
return name + '_edited' + ext
⚠️ Important Notes
Only files (not directories) are renamed.

Make sure you have write permissions for the selected folder.

This tool performs actual renaming — no undo feature is included (yet).

📄 License
This project is free to use and modify for personal or educational purposes.

👨‍💻 Author
Developed with ❤️ by Arjumand afreen tabinda
Built with Python + Streamlit

yaml
Copy
Edit

---

Let me know if you'd like to include a preview image or example screenshots in the README too — I can help generate or design tha