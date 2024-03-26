import logging
from langchain.vectorstores import FAISS
from zenml import step

from chunk import chunk_create
from models import embedding

import warnings
warnings.filterwarnings("ignore")

@step
class DataBase:
    def __init__(self) -> None:
        self.text_chunk = chunk_create()
        self.embeddings = embedding()

    def load(self):
        #Convert the Text Chunks into Embeddings and Create a FAISS Vector Store
        vector_store=FAISS.from_documents(self.text_chunk, self.embeddings)

        if not vector_store:
            logging.warning("Failed in creating Vector Database")
        
        return vector_store
    
# output = DataBase()
# print(output.load())
