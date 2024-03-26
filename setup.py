from setuptools import find_packages, setup

setup(
    name="Generative AI Project",
    description="Introducing a cutting-edge Generative AI project leveraging Langchain, Hugging Face Transformers, and ZenML for a streamlined LLMops pipeline. This innovative system is designed to create a PDF chatbot capable of engaging in natural language conversations. By harnessing the power of Langchain's linguistic insights and Hugging Face Transformers' state-of-the-art models, our project aims to revolutionize document interactions. With ZenML orchestrating the machine learning lifecycle management pipeline, we ensure scalability, reproducibility, and efficiency. Experience seamless document interactions like never before with our advanced generative AI technology.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Mahesh Gowda",
    author_email="maheshbudappa30@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    keywords="Generative AI, LLMops",
)