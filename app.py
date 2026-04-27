import streamlit as st
from pdf_reader import extract_text, extract_text_from_pdf
from summarizer import summarize_text   
from fpdf import FPDF
def create_pdf(summary_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Split long text into lines that fit the page
    for line in summary_text.split("\n"):
        pdf.multi_cell(0, 10, line)

    return pdf.output(dest="S").encode("latin-1")

st.set_page_config(page_title="AI PDF Summarizer", layout="wide")
st.title(("AI PDF Summarizer"))
st.write("Upload a PDF file to get a concise summary of its content.")
#Lets the user upload a PDF.
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")   

if uploaded_file is not None:
    st.info("Extracting text from PDF...")

    # Save uploaded file to a temporary path
    temp_path = "temp.pdf"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Now pass the file path, not the UploadedFile object
    text = extract_text(temp_path)


    if len(text.strip()) == 0:
        st.error("No readable text found in this PDF.")
    else:
        st.success("Text extracted successfully!")

        if st.button("Summarize PDF"):
            with st.spinner("Summarizing... this may take a moment"):
                summary = summarize_text(text)

            st.subheader("📌 Summary")
            st.write(summary)
            if(summary):
                st.subheader("Summary")
                st.write(summary)
                pdf_bytes = create_pdf(summary)
                st.download_button(
                    label="Download Summary as PDF",
                    data=pdf_bytes,
                    file_name="summary.pdf",
                    mime="application/pdf"
            )