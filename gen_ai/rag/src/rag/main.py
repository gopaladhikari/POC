from .generate_fake_data import generate_fake_data
from .index import index_pdf
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

pdf_path = Path.cwd() / "report.pdf"


def main():
    if not pdf_path.exists():
        print("PDF not found. Generating data...")
        generate_fake_data(output_path=pdf_path)

    # 2. Now run the indexer
    index_pdf(pdf_path)


if __name__ == "__main__":
    main()
