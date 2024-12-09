import streamlit as st
import os
st.set_page_config(page_title="Informações de Saúde - Saúde")

with open("inicio.css") as editor:
    st.markdown(f"<style>{editor.read()}</style>",unsafe_allow_html=True)

image_path = os.path.join("img", "logo.png")
st.sidebar.image(image_path)
image_url = "https://img.freepik.com/premium-vector/white-abstract-background-design_1208459-106.jpg?semt=ais_hybrid"  # Exemplo: "imagens/fundo.jpg"
# Adicione a imagem de fundo com HTML e CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


st.write('<p style="font-size:60px;text-align:center;font-weight:bold">Cadastro de Paciente</p>',unsafe_allow_html=True)
st.write('<p style="font-size:20px;text-align:center;font-weight:bold">Por favor, preencha os dados abaixo para o seu cadastro.</p>',unsafe_allow_html=True)

if "nome" in st.session_state and "email" in st.session_state and "senha" in st.session_state:
    if "cadastro" in st.session_state and st.session_state["cadastro"]:
        st.success("Seu cadastro realizado com sucesso! Seja Bem-Vindo(a)!")
    else:
        with st.form("saúde"):
            st.header("Informações de Saúde")

            altura = st.number_input("Altura (cm)", min_value=50, max_value=250, step=1, value=170)
            peso = st.number_input("Peso (kg)", min_value=10, max_value=300, step=1, value=70)
            
            enviado = st.form_submit_button("Enviar Cadastro")

        if enviado:
            if altura and peso:
                st.session_state["altura"] = altura
                st.session_state["peso"] = peso
                st.session_state["cadastro"] = True
                st.switch_page("pages\Ingestão de Água.py")
            else:
                st.error("Por favor, verifique se todos os campos estão preenchidos.")

else:
    st.warning("Realize o Cadastro para acessar.")