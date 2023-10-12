import os
import gradio as gr
from dotenv import load_dotenv
load_dotenv()
from llama_index import Prompt, VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('documentos').load_data()

TEMPLATE_STR = (
    "Nós fornecemos informações de contexto abaixo.\n"
    "---------------------\n"    
    "{context_str}"
    "\n---------------------\n"
    "Somente com base nessas informações, por favor responda à pergunta.: {query_str}.\n"
)

QA_TEMPLATE = Prompt(TEMPLATE_STR)

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine(text_qa_template=QA_TEMPLATE)

def run_code(question):    
    if question:
        answer = query_engine.query(question)         
        return str(answer)
    else:
        return "Pergunta inválida."

iface = gr.Interface(
    fn=run_code,
    inputs="text",
    outputs="text",
    title="Chatbot da Biblia Sagrada",
    description="Faça uma pergunta e obtenha uma resposta."
)

iface.launch()






