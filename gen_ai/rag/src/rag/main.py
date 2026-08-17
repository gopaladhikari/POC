from .generate_fake_data import generate_fake_data
from .index import index_pdf
from pathlib import Path
from dotenv import load_dotenv
from .chat import chat

load_dotenv()

pdf_path = Path.cwd() / "report.pdf"


def main():
    if not pdf_path.exists():
        print("PDF not found. Generating data...")
        generate_fake_data(output_path=pdf_path)
        print("Indexing the newly generated PDF...")
        index_pdf(pdf_path)
    else:
        print("PDF already exists. Skipping generation and indexing.")

    chat()


if __name__ == "__main__":
    main()
