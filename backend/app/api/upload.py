import os
import shutil
import uuid
from fastapi import APIRouter, UploadFile, File

import fitz

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


router = APIRouter()


PAPERS_DIR = "papers"
DB_DIR = "chroma_db"



@router.post("/upload")
async def upload(
    file: UploadFile = File(...)
):

    try:

        print("📄 Upload started")


        os.makedirs(
            PAPERS_DIR,
            exist_ok=True
        )


        file_path = os.path.join(
            PAPERS_DIR,
            file.filename
        )


        # save file

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )


        print("✅ PDF saved")



        # Extract text

        pdf = fitz.open(file_path)


        documents = []


        for page_number,page in enumerate(pdf):

            text = page.get_text()


            if text.strip():

                documents.append(

                    Document(

                        page_content=text,

                        metadata={

                            "source": file.filename,

                            "page": page_number + 1

                        }

                    )

                )


        print(
            f"Extracted pages: {len(documents)}"
        )



        # Split

        splitter = RecursiveCharacterTextSplitter(

            chunk_size=1000,

            chunk_overlap=150

        )


        chunks = splitter.split_documents(
            documents
        )


        print(
            f"Chunks created: {len(chunks)}"
        )



        # Remove old DB safely

        if os.path.exists(DB_DIR):

            try:

                shutil.rmtree(DB_DIR)

            except PermissionError:

                print(
                    "Old chroma still locked, skipping delete"
                )



        embeddings = OllamaEmbeddings(

            model="nomic-embed-text"

        )

        collection_name="current_paper"

        Chroma.from_documents(

            documents=chunks,

            embedding=embeddings,

            persist_directory=DB_DIR,

            collection_name=collection_name

        )


        print(
            "✅ Vector database created"
        )


        return {

            "message":
            "Paper processed successfully"

        }


    except Exception as e:


        print(
            "UPLOAD ERROR:",
            e
        )


        return {

            "error":str(e)

        }