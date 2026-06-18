from ingestion.parser import extract_text
from ingestion.income_tax_section_chunker import split_income_tax_sections

text = extract_text(
    "documents/Income_Tax_Act.pdf"
)

sections = split_income_tax_sections(text)

print("Sections Found:", len(sections))

for s in sections[:5]:
    print(s["section"])