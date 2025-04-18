import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import os
import io

# 💾 Create folder to save processed images
OUTPUT_FOLDER = "generated_images"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# 🧱 Page title and instructions
st.title("🖼️ Image Processing App")
st.markdown("Upload an image, tweak the settings from the sidebar, and download your customized version!")

# 📤 Image uploader
uploaded_file = st.file_uploader("📁 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    base_name = os.path.splitext(uploaded_file.name)[0]

    st.image(image, caption="📸 Original Image", use_column_width=True)

    # 🎚️ Sidebar controls
    with st.sidebar:
        st.header("🎛️ Adjust Image Settings")
        brightness = st.slider("✨ Brightness", 0.5, 3.0, 1.5)
        contrast = st.slider("🎨 Contrast", 0.5, 3.0, 1.8)
        apply_blur = st.checkbox("🌀 Apply Blur")
        convert_gray = st.checkbox("⚫ Convert to Grayscale")

    # 🛠️ Apply enhancements
    processed_image = ImageEnhance.Brightness(image).enhance(brightness)
    processed_image = ImageEnhance.Contrast(processed_image).enhance(contrast)

    if apply_blur:
        processed_image = processed_image.filter(ImageFilter.BLUR)

    if convert_gray:
        processed_image = processed_image.convert("L")

    # 📸 Display processed image
    st.subheader("✅ Processed Image")
    st.image(processed_image, use_column_width=True)

    # 💾 Save image to output folder
    processed_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_edited.png")
    processed_image.save(processed_path)

    # 📥 Prepare image for download
    img_bytes = io.BytesIO()
    processed_image.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    # 🔽 Download button
    st.download_button(
        label="⬇️ Download Processed Image",
        data=img_bytes,
        file_name=f"{base_name}_edited.png",
        mime="image/png"
    )

    # ✅ Success message
    st.success(f"Image saved to `{OUTPUT_FOLDER}` folder.")

# 🚀 To run this app:
# Open terminal in the folder and type: streamlit run app.py
