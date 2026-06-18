from ingestion.parser import extract_text

text = extract_text("documents/GST_ACT.pdf")

keywords = [
"29.",
"29. Cancellation",
"Cancellation of registration",
"Revocation of cancellation"
]

for keyword in keywords:


    pos = text.lower().find(keyword.lower())

print("\nKeyword:", keyword)
print("Position:", pos)

if pos != -1:
    print(text[pos:pos+1500])


