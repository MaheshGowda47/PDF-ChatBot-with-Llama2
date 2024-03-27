import logging
from langchain.chains import RetrievalQA
from zenml import step, pipeline

from source.vector_store import DataBase
from source.prompt import prompt
from source.models import llm_model

@step
class chain_link:
    def __init__(self) -> None:
        self.llm = llm_model()
        self.vector_store = DataBase()
        self.qa_prompt = prompt()

    def load(self):
        chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type='stuff',
            retriever=self.vector_store.load().as_retriever(search_kwargs={'k': 2}),
            return_source_documents=False,
            chain_type_kwargs={'prompt': self.qa_prompt}
        )
        
        return chain

