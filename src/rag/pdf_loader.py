from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path):

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    for doc in documents:
        doc.page_content = doc.page_content.replace("\n", " ")

    return documents