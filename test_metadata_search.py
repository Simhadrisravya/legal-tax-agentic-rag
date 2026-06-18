from metadata_search import metadata_search

chunks = metadata_search(
    "What is Section 29 of GST Act?",
    "GST_ACT.pdf"
)

print(
    "Chunks Found:",
    len(chunks)
)

print()
print(chunks[0][:1000])