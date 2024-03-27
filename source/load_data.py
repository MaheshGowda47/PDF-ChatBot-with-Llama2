import logging
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from zenml import step

@step
class Data:
    def __init__(self, data_path) -> None:
        self.data_path = data_path

    def load(self):
        loader = DirectoryLoader(self.data_path, glob="*.pdf", loader_cls=PyPDFLoader)
        data = loader.load()
        if not data:
            logging.warning("Failed to load the Data Directory")

        return data
    