import os
from dotenv import load_dotenv
load_dotenv()

import logging
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import CTransformers
from zenml import step

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

@step
def embedding():
    #Load the Embedding Model
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', 
                                     model_kwargs={'device':'cpu'})
    if not embeddings:
        logging.warning("Problem in loading Embedding model from HuggingFace")
    
    return embeddings


@step
def llm_model():
    #Load the Llma2 model
    llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                      model_type="llama",
                      config={'max_new_tokens':128,
                              'temperature':0.01})
    
    if not llm:
        logging.warning("Problem in loading Llma model from Directory")

    return llm  