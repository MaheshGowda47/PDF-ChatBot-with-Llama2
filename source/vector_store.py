import logging
from langchain_community.vectorstores import FAISS
from zenml import step 

@step
class DataBase:
    def __init__(self, chunks, embeddings) -> None:
        self.chunks = chunks
        self.embeddings = embeddings

    def load(self):
        #Convert the Text Chunks into Embeddings and Create a FAISS Vector Store
        vector_store=FAISS.from_documents(self.chunks, self.embeddings)

        if not vector_store:
            logging.warning("Problem occured in creating Vector DataBase")

        return vector_store

        
# from load_data import Data
# from create_chunk import chunks
# from models import embedding
# data = Data("data")
# loaded_data = data.load()
# chunk = chunks(loaded_data)
# created_chunks = chunk.load()
# embedding = embedding()

# print(DataBase(created_chunks, embedding).load())