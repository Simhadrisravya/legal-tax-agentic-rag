from load_metadata import load_metadata

metadata = load_metadata()

documents = set()

for item in metadata:


    documents.add(
    item.get("document")
)


print(documents)
