from ingestion.parser import extract_text

pdf_file = "documents/GST_ACT.pdf"

text = extract_text(pdf_file)

print(text[:1000])