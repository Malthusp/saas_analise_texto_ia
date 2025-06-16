import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Chave da API Gemini não encontrada. Certifique-se de que a variável de ambiente GEMINI_API_KEY está definida no arquivo .env.")
    st.stop() 

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Analisador de Texto com IA", page_icon="📝")

st.title("📝 Analisador de Texto com IA")
st.markdown("Seu SaaS para análise de sentimentos, resumo e extração de palavras-chave.")

user_text = st.text_area("Cole seu texto aqui para análise:", height=250)

if st.button("Analisar Texto"):
    if user_text:
        with st.spinner("Analisando... Por favor, aguarde."):
            try:
                prompt_sentimento = f"Qual o sentimento predominante (positivo, negativo, neutro ou misto) do seguinte texto? Responda de forma concisa em uma única palavra ou uma breve frase: '{user_text}'"
                response_sentimento = model.generate_content(prompt_sentimento)
                sentimento = response_sentimento.text.strip()

                prompt_resumo = f"Faça um resumo conciso do seguinte texto, com no máximo 3 frases: '{user_text}'"
                response_resumo = model.generate_content(prompt_resumo)
                resumo = response_resumo.text.strip()

                prompt_keywords = f"Liste as 5 principais palavras-chave do seguinte texto, separadas por vírgulas: '{user_text}'"
                response_keywords = model.generate_content(prompt_keywords)
                keywords = response_keywords.text.strip()

                st.subheader("Resultados da Análise:")

                st.write(f"**Sentimento:** {sentimento}")
                st.write(f"**Resumo:** {resumo}")
                st.write(f"**Palavras-chave:** {keywords}")

            except Exception as e:
                st.error(f"Ocorreu um erro ao processar seu texto: {e}")
                st.info("Por favor, tente novamente com um texto diferente ou verifique sua conexão com a internet/chave da API.")
    else:
        st.warning("Por favor, insira um texto para análise.")

st.sidebar.header("Sobre")
st.sidebar.info(
    "Este é um SaaS de exemplo construído com Streamlit e a API Gemini para "
    "demonstrar processamento de dados com IA."
)
