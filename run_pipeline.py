from source.load_data import Data
from source.create_chunk import chunks
from source.vector_store import DataBase
from source.models import llm_model, embedding
from source.prompt import prompt
from source.run_chain import chain

from zenml import pipeline

# @pipeline
def run_pipeline():
    loaded_data = Data("data").load()
    # print("Loaded data:", loaded_data)

    chunk = chunks(loaded_data).load()
    # print("Created chunks:", chunk)

    embeddings = embedding()

    vector_store = DataBase(chunk, embeddings).load()

    llm = llm_model()
    qa_prompt = prompt()

    run_chain = chain(llm, vector_store, qa_prompt)
    return run_chain

# if __name__ == "__main__":
#     print(run_pipeline())

# Dont run this file changes have maded