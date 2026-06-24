import os
import shutil
import fitz

from fastapi import APIRouter, UploadFile, File

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


router = APIRouter()

BASE_DIR = "app/data/chats"


@router.post("/upload/{chat_id}")
async def upload_pdf(
    chat_id: str,
    file: UploadFile = File(...)
):

    try:

        chat_path = os.path.join(
            BASE_DIR,
            chat_id
        )

        if not os.path.exists(chat_path):

            return {
                "error": "Chat not found"
            }

        papers_dir = os.path.join(
            chat_path,
            "papers"
        )

        chroma_dir = os.path.join(
            chat_path,
            "chroma"
        )

        pdf_path = os.path.join(
            papers_dir,
            file.filename
        )

        with open(pdf_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        print(f"Saved: {file.filename}")

        pdf = fitz.open(pdf_path)

        docs = []

        for page_num, page in enumerate(pdf):

            text = page.get_text()

            if text.strip():

                docs.append(

                    Document(

                        page_content=text,

                        metadata={
                            "source": file.filename,
                            "page": page_num + 1
                        }

                    )

                )

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150
        )

        chunks = splitter.split_documents(docs)

        embeddings = OllamaEmbeddings(
            model="nomic-embed-text"
        )

        vectorstore = Chroma(
            persist_directory=chroma_dir,
            embedding_function=embeddings
        )

        vectorstore.add_documents(chunks)

        return {

            "message":
            f"{file.filename} uploaded successfully",

            "pages":
            len(docs),

            "chunks":
            len(chunks)

        }

    except Exception as e:

        print("UPLOAD ERROR:", e)

        return {
            "error": str(e)
        }