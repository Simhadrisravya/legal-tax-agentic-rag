from ingestion.parser import extract_text
import re

text = extract_text("documents/GST_ACT.pdf")

matches = re.finditer(
r'\n\s*29.',
text
)

for match in matches:


    start = max(0, match.start() - 300)
    end = match.start() + 1500

print(text[start:end])
print("\n" + "="*80 + "\n")

