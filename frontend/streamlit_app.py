import streamlit as st
from PIL import Image
from gradio_client import Client

# Nome do arquivo para armazenar o contador de acessos
contador_arquivo = "contador_acessos.txt"

# Função para ler o valor atual do contador de acessos
def ler_contador():
    try:
        with open(contador_arquivo, "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# Função para atualizar e salvar o contador de acessos
def atualizar_contador():
    total_acessos = ler_contador()
    total_acessos += 1
    with open(contador_arquivo, "w") as file:
        file.write(str(total_acessos))
    return total_acessos

image = Image.open('bíblia1.jpg')

# Título da aplicação Streamlit
st.title("Pergunte para a Bíblia Sagrada")
st.image('bíblia1.jpg', caption='Biblia Sagrada')

# Criar um campo de entrada de texto para a pergunta
question = st.text_input("Digite sua pergunta:")

# Botão para fazer a previsão
if st.button("Enviar"):
    # Incrementar e obter o contador de acessos
    total_acessos = atualizar_contador()
    
    # Criar uma instância do cliente Gradio
    client = Client("FabioSantos/biblia", hf_token="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")
    
    # Fazer uma previsão com a pergunta inserida
    result = client.predict(question, api_name="/predict")
    
    # Exibir a resposta
    st.write("Resposta da Bíblia:")
    st.write(result)

# Exibir o número total de acessos
st.write(f"Número total de acessos: {ler_contador()}")

# Nota explicativa
st.markdown("*Desenvolvido por Prof.Dr.Fabio Santos (fssilva@uea.edu.br)*")


