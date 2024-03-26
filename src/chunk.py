import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter
from zenml import step

from load_pdf import load_data

@step
class chunk:
    def __init__(self) -> None:
        self.data_path = load_data()

    def load(self):
        data_path = self.data_path
        if not data_path:
            logging.warning("Problem in Data Directory")
        return data_path
    
def chunk_create():
    documents = chunk()

    #Split Text into Chunks
    text_splitter=RecursiveCharacterTextSplitter(
                                             chunk_size=500,
                                             chunk_overlap=50)
    text_chunks=text_splitter.split_documents(documents.load())

    if not text_chunks:
        logging.warning("Problem in creating chunks")
    return text_chunks

# if __name__ =="__main__":
#     output = chunk_create()
#     print(output)