import os
import streamlit as st

def bulk_rename(directory, rename_condition):
    messages = []
    try:
        files = os.listdir(directory)
        messages.append(f"📁 Found {len(files)} items in '{directory}'")

        for original_name in files:
            original_path = os.path.join(directory, original_name)

            if os.path.isfile(original_path):
                new_name = rename_condition(original_name)
                new_path = os.path.join(directory, new_name)

                os.rename(original_path, new_path)
                messages.append(f"✅ Renamed: {original_name} → {new_name}")
    except Exception as error:
        messages.append(f"❌ Error: {error}")
    return messages

def rename_condition(filename):
    # Custom logic goes here
    return 'new_' + filename

# Streamlit UI
st.title("🔄 Bulk Rename Utility")
st.markdown("Rename all files in a folder based on your logic.")

directory = st.text_input("📂 Enter the full directory path")

if st.button("🚀 Start Renaming"):
    if directory:
        results = bulk_rename(directory, rename_condition)
        for msg in results:
            if msg.startswith("✅"):
                st.success(msg)
            elif msg.startswith("❌"):
                st.error(msg)
            else:
                st.info(msg)
    else:
        st.warning("Please enter a valid directory path.")

