from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os


load_dotenv()


def get_embeddings():

    hf_token = os.getenv("HF_TOKEN")


    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={
            "token": hf_token
        }
    )

    return embeddings