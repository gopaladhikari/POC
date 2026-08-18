from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from pathlib import Path


from .generate_fake_data import generate_fake_data
from .index import index_pdf


def initialize_database():
    qdrant_url = "http://localhost:6333"
    collection_name = "test"
    pdf_path = Path.cwd() / "report.pdf"

    # 1. Initialize the raw Qdrant client to check the server
    client = QdrantClient(url=qdrant_url)

    # 2. Check if the collection exists safely
    if not client.collection_exists(collection_name=collection_name):
        print(
            f"⚠️ Collection '{collection_name}' not found. Initializing build process..."
        )

        # Generate the PDF if it's missing
        if not pdf_path.exists():
            print("Generating fake PDF data...")
            generate_fake_data(output_path=pdf_path)

        print("Indexing PDF into Qdrant...")

        vector_store = index_pdf(pdf_path)

    else:
        print(f"✅ Collection '{collection_name}' found. Connecting directly...")
        embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

        # Safely connect to the existing collection
        vector_store = QdrantVectorStore.from_existing_collection(
            url=qdrant_url,
            collection_name=collection_name,
            embedding=embeddings,
        )

    return vector_store
