import streamlit as st
from PIL import Image
import pytesseract

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image, lang='eng+hin')
    return text

def main():
    st.title("OCR and Document Search Prototype")
    st.write("Upload an image to extract text and search within the text.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Extracting text...")
        extracted_text = extract_text_from_image(image)
        st.write(extracted_text)

        search_query = st.text_input("Enter keyword to search:")
        if search_query:
            if search_query.lower() in extracted_text.lower():
                st.write(f"Keyword '{search_query}' found in the text.")
            else:
                st.write(f"Keyword '{search_query}' not found in the text.")

if __name__ == "__main__":
    main()
