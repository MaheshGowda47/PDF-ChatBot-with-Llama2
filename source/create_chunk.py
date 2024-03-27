import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter
from zenml import step 

from source.load_data import Data

@step
class chunks:
    def __init__(self) -> None:
        self.loaded_data = Data()

    def load(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        text_chunk = text_splitter.split_documents(self.loaded_data.load())

        if not text_chunk:
            logging.warning("Problem in creating chunks")
        
        # print(len(text_chunk))
        return text_chunk


