from ingestion.parser import extract_text
from ingestion.chunker import split_text
from ingestion.embeddings import create_vector_store
from ingestion.section_chunker import split_by_sections
from ingestion.income_tax_section_chunker import split_income_tax_sections

from metadata_store import save_metadata

import faiss
import numpy as np
import os

os.makedirs("vector_db", exist_ok=True)

pdf_files = ["GST_ACT.pdf", "GST_Rules.pdf", "Income_Tax_Act.pdf"]

all_chunks = []
metadata = []

print(f"Found {len(pdf_files)} PDFs")
for pdf in pdf_files:
    print(f"Processing: {pdf}")
    pdf_path = f"documents/{pdf}"
    text = extract_text(pdf_path)

    if pdf == "GST_ACT.pdf":
        sections = split_by_sections(text)
        for section in sections:
            all_chunks.append(section["text"])
            metadata.append({"document": pdf, "section": section["section"], "text": section["text"]})

    elif pdf == "Income_Tax_Act.pdf":
        sections = split_income_tax_sections(text)
        print("Income Tax Sections Found:", len(sections))
        for section in sections:
            all_chunks.append(section["text"])
            metadata.append({"document": pdf, "section": section["section"], "text": section["text"]})

    else:
        chunks = split_text(text)
        for chunk in chunks:
            all_chunks.append(chunk)
            metadata.append({"document": pdf, "text": chunk})

print(f"Total Chunks: {len(all_chunks)}")

docs = {}
for item in metadata:
    docs[item["document"]] = docs.get(item["document"], 0) + 1

print("\nDocument Counts:")
print(docs)

index, embeddings = create_vector_store(all_chunks)
faiss.write_index(index, "vector_db/legal_index.faiss")
np.save("vector_db/legal_embeddings.npy", embeddings)

with open("vector_db/chunks.txt", "w", encoding="utf-8") as f:
    for chunk in all_chunks:
        f.write(chunk)
        f.write("\n<<END_CHUNK>>\n")

save_metadata(metadata)

print()
print("================================")
print("Multi-PDF Index Created")
print("Vectors :", index.ntotal)
print("Chunks  :", len(all_chunks))
print("Metadata:", len(metadata))
print("================================")
