import logging
from langchain.chains import RetrievalQA
from zenml import step, pipeline

@step
class chain:
    def __init__(self, llm, vector_store, qa_prompt) -> None:
        self.llm = llm
        self.vector_store = vector_store
        self.qa_prompt = qa_prompt

    def load(self):
        chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type='stuff',
            retriever=self.vector_store.as_retriever(search_kwargs={'k': 2}),
            return_source_documents=False,
            chain_type_kwargs={'prompt': self.qa_prompt}
        )
        return chain
    




