import streamlit as st
from PIL import Image

# change style of buttons-----------------------------------
st.markdown("""
    <style>
    .stButton>button {
        background-color: #030164;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 24px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# UI page configuration-----------------------------------
st.set_page_config(
    page_title="RGB to Grayscale Converter",
    page_icon="🖼️",
    layout="centered",
)
st.title("🖼️ RGB to Grayscale Converter")
st.write("Upload an RGB image to convert it to grayscale.")

# image file uploader---------------------------------------
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "bmp", "gif"]) 

# Display image if uploaded---------------------------------
if uploaded_file is not None:
    # Open the uploaded image
    img = Image.open(uploaded_file)

    st.success("Image uploaded successfully!")

    # Display original image
    st.subheader("Original Image")
    st.image(
        img,
        caption=uploaded_file.name,
        use_container_width=True
    )

    # Convert to grayscale
    grayscale_img = img.convert("L")

    # Display grayscale image
    st.subheader("Converted Grayscale Image")
    st.image(
        grayscale_img,
        caption="Grayscale version",
        use_container_width=True
    )
    # save the grayscale image to a file using save button file name with user input-------
    save_filename = st.text_input("Enter filename to save the grayscale image (without extension):", "grayscale_image")
    if st.button("Save Grayscale Image"):
        if save_filename:
            grayscale_img.save(f"{save_filename}.png")
            st.success(f"Grayscale image saved as {save_filename}.png")
        else:
            st.error("Please enter a valid filename.")
    