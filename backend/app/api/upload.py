from fastapi import APIRouter, UploadFile
import shutil
import os

from app.rag.loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.vectorstore import create_vectorstore


router=APIRouter()


@router.post("/upload")
async def upload(file:UploadFile):


    os.makedirs(
        "papers",
        exist_ok=True
    )


    path=f"papers/{file.filename}"


    with open(path,"wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    docs=load_pdf(path)

    chunks=split_documents(docs)


    create_vectorstore(chunks)


    return {

        "message":"Paper processed successfully",

        "pages":len(docs),

        "chunks":len(chunks)

    }