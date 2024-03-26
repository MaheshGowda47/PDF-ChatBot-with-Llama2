import logging
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader
from zenml import step

@step
class LoadPDF:
    def __init__(self) -> None:
        self.data_path = "data"

    def load(self):
        data_path = self.data_path
        if not data_path:
            logging.warning("Problem in Data Directory")
        return data_path
    
def load_data():
    data_path = LoadPDF()
    loader=DirectoryLoader(data_path.load(), glob="*.pdf", loader_cls=PyPDFLoader)
    data = loader.load()

    if not data:
        logging.warning("Problem in loading data")
    return data

# if __name__ == "__main__":
#     output = load_data()
#     print(output)