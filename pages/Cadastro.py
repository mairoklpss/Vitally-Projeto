import streamlit as st
from time import sleep
import os
# Configuração da página
st.set_page_config(page_title="Cadastro de Paciente - Saúde")

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
with open("cadastro.css") as editor:
    st.markdown(f"<style>{editor.read()}</style>",unsafe_allow_html=True)



# Título da página
st.write('<p style="font-size:60px;font-weight:Bold;text-align:center">Cadastro de Paciente</p>', unsafe_allow_html=True)
st.write('<p style="font-size:20px;text-align:center;font-weight:bold">Por favor, preencha os dados abaixo para o seu cadastro.</p>',unsafe_allow_html=True)

st.markdown("""
    <style>
        /* Cor do fundo do campo de texto */
        .stTextInput>div>div>input {
            background-color: #f0f8ff;  /* Cor de fundo (exemplo: Alice Blue) */
            color: #333333;
}
        .stTextInput>div>div>input::placeholder {
            color: #333333;
}
    </style>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    /* Altera a borda do st.text_input */
    .stTextInput input {
        border: 2px solid cyan;  /* Cor da borda */
    }
    </style>
    """, 
    unsafe_allow_html=True
)
if "cadastro_realizado" in st.session_state and st.session_state["cadastro_realizado"]:
    st.success("Cadastro realizado com sucesso! Seja Bem-Vindo(a)!")
else:
  

    with st.form("cadastro"):
        # Informações pessoais
        nome = st.text_input("Nome", placeholder = "Digite seu nome")
        sexo = st.radio("Sexo", ["Masculino", "Feminino"])
        email = st.text_input("Email", placeholder= "emailaqui@gmail.com")
        senha = st.text_input("Senha", placeholder= "(mín 8 caracteres)", type="password")
        telefone = st.text_input("Telefone", placeholder= "(**) *****-****")
        enviado = st.form_submit_button("Continue")

# Exibe mensagem após envio do formulário
    if enviado:
        if nome == "" or email == "" or senha == "" and len(senha) < 8 or telefone == "":
            st.error("Por favor, preencha todos os campos obrigatórios.") 
        elif nome and email and telefone and senha and len(senha) < 8:
            st.error("A senha deve ter no mínimo 8 caracteres.")       
        elif nome == "" and email == "" and senha == "" and telefone == "":
            st.error("Por favor, preencha todos os campos obrigatórios.") 
        elif "@" not in email:
            st.error("Digite seu email corretamente")
        else:
            st.session_state["nome"] = nome
            st.session_state["sexo"] = sexo
            st.session_state["email"] = email
            st.session_state["senha"] = senha
            st.session_state["telefone"] = telefone
            st.session_state["cadastro_realizado"] = True           
            st.switch_page("pages/Informações de Saúde.py")
import streamlit as st

# Injetar CSS personalizado