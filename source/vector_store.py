import logging
from langchain_community.vectorstores import FAISS
from zenml import step 

from source.create_chunk import chunks
from source.models import embedding

@step
class DataBase:
    def __init__(self) -> None:
        self.chunks = chunks()
        self.embeddings = embedding()

    def load(self):
        #Convert the Text Chunks into Embeddings and Create a FAISS Vector Store
        vector_store=FAISS.from_documents(self.chunks.load(), self.embeddings)

        if not vector_store:
            logging.warning("Problem occured in creating Vector DataBase")

        return vector_store
