from load_metadata import load_metadata

metadata = load_metadata()

print("Records:", len(metadata))

print("\nFirst Record:\n")

print("Document:", metadata[0]["document"])

if "section" in metadata[0]:
    print("Section:", metadata[0]["section"])

print("Text Preview:")
print(metadata[0]["text"][:300])

