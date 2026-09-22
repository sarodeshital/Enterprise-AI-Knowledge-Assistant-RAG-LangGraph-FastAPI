from pypdf import PdfReader
def extract_text(path):
    reader=PdfReader(path)
    return "".join(page.extract_text() or "" for page in reader.pages)
