import streamlit as st
from bar_code_qr_code_recognition import process_image

st.title("Barcode and QR Code Recognition")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image,no_of_detections,result = process_image(uploaded_file)
    if no_of_detections:
        st.image(image, caption="Uploaded Image")
        st.write(result)
    else:
        st.write("No barcode or QR code detected in image")