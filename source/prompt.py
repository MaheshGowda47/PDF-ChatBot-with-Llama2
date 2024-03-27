import logging
from langchain import PromptTemplate
from zenml import step

@step
def prompt():

    template="""Use the following pieces of information to answer the user's question.
        If you dont know the answer just say you know, don't try to make up an answer.

        Context:{context}
        Question:{question}

        Only return the helpful answer below and nothing else
        Helpful answer
        """

    qa_prompt=PromptTemplate(template=template, input_variables=['context', 'question'])

    if not qa_prompt:
        logging.warning("Problem occured in prompt template")

    return qa_prompt

print(prompt())