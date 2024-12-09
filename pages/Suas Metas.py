
import streamlit as st
import os


with open("mt.css") as editor:
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

st.write('<p style="font-size:60px;font-weight:bold;text-align:center">Suas Metas!</p>',unsafe_allow_html=True)
st.write('<p style="font-size:20px;text-align:center;font-weight:bold">Escreva as suas metas do dia e marque-as quando você realizá-las.</p>',unsafe_allow_html=True)

# Verificando se a lista de metas já existe no estado da sessão
if 'lista_itens' not in st.session_state:
    st.session_state.lista_itens = []

if "nome" in st.session_state and "email" in st.session_state and "senha" in st.session_state and "peso" in st.session_state:
    # Função para marcar itens de uma lista
    def marcar_itens(lista):
        itens_selecionados = []
        for i, item in enumerate(lista):  # Usando enumerate para obter índice e item
            if st.checkbox(f'{item}', key=f"opcao_{i}"):  # Cada item recebe um checkbox com chave única
                itens_selecionados.append(item)
                
        return itens_selecionados

    # Interface para adicionar novas metas
    with st.form(key='form_lista'):
        itens = st.text_input("Escreva uma meta:", placeholder="Ex: Atingir minha meta de ingestão de água...")
        enviado = st.form_submit_button("Adicionar Meta")
        
        if enviado and itens:
            # Adiciona a nova meta à lista no estado da sessão
            st.session_state.lista_itens.append(itens)
            st.success(f'Meta "{itens}" adicionada com sucesso!')

    # Chamando a função para marcar os itens
    st.header("Suas metas para hoje:")
    itens_selecionados = marcar_itens(st.session_state.lista_itens)

    # Exibindo a lista de metas e os itens selecionados
    if st.session_state.lista_itens:
        if itens_selecionados:
            st.header('- Você concluiu as seguintes metas:')
            for item in itens_selecionados:
                st.write("-", item, "✅")
        else:
            st.info('Nenhuma meta concluída ainda.')
    else:
        st.info('Nenhuma meta adicionada ainda.')

    navegar = st.button("Ir para Ingestão de Água")
    if navegar:
        st.switch_page("pages/Ingestão de Água.py")

    navegar1 = st.button("Ir para Registro de Atividades")
    if navegar1:
        st.switch_page("pages/Registro de Atividades.py")        

else:
    st.warning("Realize o Cadastro para acessar.")