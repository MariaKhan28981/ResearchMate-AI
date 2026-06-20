import fitz
from langchain_core.documents import Document


def load_pdf(path):

    pdf = fitz.open(path)

    documents=[]

    for page_no,page in enumerate(pdf):

        text = page.get_text()

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "page":page_no+1,
                    "source":path
                }
            )
        )

    return documents