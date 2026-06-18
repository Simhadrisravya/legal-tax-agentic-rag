from ingestion.parser import extract_text

text = extract_text(
    "documents/Income_Tax_Act.pdf"
)

keyword = "80C"

pos = text.find(keyword)

print("Position:", pos)

print(
    text[pos:pos+5000]
)