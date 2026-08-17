from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from pathlib import Path


def index_pdf(pdf_path: Path):
    # Load the PDF
    loader = PyPDFLoader(str(pdf_path))

    docs = loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)

    chunks = text_splitter.split_documents(documents=docs)

    # Vector embedding

    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")

    vectors_store = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        url="http://localhost:6333",
        collection_name="test",
    )

    print("Indexing completed")

    return vectors_store
