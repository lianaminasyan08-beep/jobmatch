from io import BytesIO
from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_upload(uploaded_file):

    content = uploaded_file.read()
    name = uploaded_file.name.lower()

    try:
        if name.endswith(".pdf"):
            reader = PdfReader(BytesIO(content))
            pages = []
            for p in reader.pages:
                pages.append(p.extract_text() or "")
            text = "\n".join(pages)
            return text

        if name.endswith(".docx"):
            doc = Document(BytesIO(content))
            paragraphs = [p.text for p in doc.paragraphs]
            return "\n".join(paragraphs)


        try:
            return content.decode("utf-8", errors="ignore")
        except Exception:
            return str(content)
    finally:
        try:
            uploaded_file.seek(0)
        except Exception:
            pass
