#importação do Streamlit
import streamlit as st
import time
import os
#Junção do Streamlit com CSS
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


def tela_inicial():
    st.title("Bem-Vindo ao *Vitally*!")
    st.write('<p style="font-size:25px;color:black;text-align:center">Bem-vindo ao Vitally, o seu aplicativo completo para o cuidado com a saúde e bem-estar! com um design intuitivo e recursos inovadores, o Vittaly ajuda você a monitorar, organizar e melhorar sua qualidade de vida, oferecendo suporte diário para suas necessidades de saúde.</p>', unsafe_allow_html=True)
    col1,col2,col3 = st.columns(3) 
    with col1:
        st.title("*Metas Personalizadas*")
        st.write('<p style="color:black;font-size:20px;">Registre suas atividades diárias e acompanhe seu progresso em busca de uma vida mais ativa e saudável. O Vitally permite definir metas personalizadas para incentivar um estilo de vida equilibrado.</p>',unsafe_allow_html=True)
    with col2:
        st.title("*Alarmes Personalizados*")
        st.write('<p style=color:black;font-size:20px;">Receba lembretes ao longo do dia para beber água no momento certo. Personalize o intervalo e o volume de água que deseja ingerir, com lembretes que se adaptam ao seu estilo de vida.</p>',unsafe_allow_html=True)
    with col3:
        st.header("*Gestao Personalizada*")
        st.write('<p style="color:black;font-size:20px;">O Vitally calcula, com base no seu peso, idade e nível de atividade física, a quantidade ideal de água para você. Além disso, você pode definir metas específicas para atingir seus objetivos pessoais de hidratação.</p>',unsafe_allow_html=True)
    st.write("""| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |""")
    bt1 = st.button("Cadastrar")
    if bt1:
        st.switch_page("pages/Cadastro.py")
    


    return


tela_inicial()