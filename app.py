import streamlit as st
import fitz ##this is pymuodf , a library that reads the pdf
from groq import Groq ##imports groq so that we can talk to the LLM


st.title("AI PDF SUMMARIZER")
st.write("Upload a PDF and get instant summary")

api_key=st.text_input("Enter your API key here ",type="password")
uploaded_file=st.file_uploader("Upload your PDF",type="pdf")

if uploaded_file is not None:
    doc=fitz.open(stream=uploaded_file.read(),filetype="pdf")
    text=""
    for page in doc:
        text+=page.get_text()
    st.success("PDF UPLOADED SUCCESSFULLY")

if st.button("Summarize PDF "):
    if api_key=="":
        st.warning("Please enter your Groq Api key !")
    else:
        client=Groq(api_key=api_key)
        with st.spinner("Summarizing....."):
            response=client.chat.completions.create(
               model="llama-3.3-70b-versatile",
               messages=[{"role": "user", "content": f"Summarize this text in simple bullet points:\n\n{text[:3000]}"}]
           )
            summary = response.choices[0].message.content
            st.subheader("Summary:")
            st.write(summary)
           