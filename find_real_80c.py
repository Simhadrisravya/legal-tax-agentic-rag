from ingestion.parser import extract_text

print("STARTED")

text = extract_text(
    "documents/Income_Tax_Act.pdf"
)

print("TEXT LENGTH:", len(text))

keyword = "80C."

positions = []

start = 0

while True:

    pos = text.find(keyword, start)

    if pos == -1:
        break

    positions.append(pos)

    start = pos + 1

print("OCCURRENCES FOUND:", len(positions))

for pos in positions[:10]:

    print("\nPOSITION:", pos)
    print(text[pos:pos+300])