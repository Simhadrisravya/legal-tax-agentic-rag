from ingestion.parser import extract_text
from ingestion.chunker import split_text

pdf = "documents/GST_ACT.pdf"

text = extract_text(pdf)

chunks = split_text(text)

print("Total Chunks:", len(chunks))
print()
print(chunks[0])