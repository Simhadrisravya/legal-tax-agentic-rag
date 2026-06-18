from ingestion.parser import extract_text
from ingestion.section_chunker import split_by_sections

text = extract_text(
"documents/GST_ACT.pdf"
)

sections = split_by_sections(text)

print("Sections Found:", len(sections))

for section in sections[:5]:


    print("\nSECTION:", section["section"])
    print(section["text"][:500])
