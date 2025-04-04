# iMPORTAR AS BIBLIOTECAS
import streamlit as st
import fitz

# função para extrair os arquivos     
def extract_files(uploader):
    text = ""
    for pdf in uploader:
        with fitz.open(stream=pdf.read(), filetype="pdf") as doc: 
            for page in doc:
                text += page.get_text("text") 
    return text
    
    
# CRIAR A INTERFACE
def main():
    st.title("O nome do meu sistema inteligente")
    with st.sidebar:
        st.header("UPLoader Files")
        uploader = st.file_uploader("Adicione arquivos", type="pdf", accept_multiple_files=True)
    if uploader:
        text = extract_files(uploader)
        st.session_state["document-text"] = text
    user_input = st.text_input("Digite a sua pergunta")



if __name__ == "__main__":
    main()