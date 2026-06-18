# search_gst.py

from ingestion.parser import extract_text

text = extract_text("documents/GST_ACT.pdf")

print("Length:", len(text))

keyword = "Cancellation of registration"

position = text.find(keyword)

print("Position:", position)

if position != -1:
    start = max(0, position - 1000)
    end = position + 2000

    print(text[start:end])

else:
    print("Keyword not found")

