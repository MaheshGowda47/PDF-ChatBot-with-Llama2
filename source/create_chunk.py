import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter
from zenml import step 

@step
class chunks:
    def __init__(self, loaded_data) -> None:
        self.loaded_data = loaded_data

    def load(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        text_chunk = text_splitter.split_documents(self.loaded_data)

        if not text_chunk:
            logging.warning("Problem in creating chunks")
        
        # print(len(text_chunk))
        return text_chunk


