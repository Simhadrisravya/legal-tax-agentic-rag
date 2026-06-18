from ingestion.parser import extract_text
import re

text = extract_text("documents/GST_ACT.pdf")

matches = re.findall(
r'\n\s*(\d+).\s',
text
)

print("Sections Found:", len(matches))
print(matches[:50])
