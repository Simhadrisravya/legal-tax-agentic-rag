from load_metadata import load_metadata

metadata = load_metadata()

income_tax_items = [
    item for item in metadata
    if item["document"] == "Income_Tax_Act.pdf"
]

print("Total Income Tax Act records:", len(income_tax_items))

# Look at a slice from early in the list — TOC-derived junk would show up here
for item in income_tax_items[:15]:
    section_id = item.get("section", "MISSING")
    preview = item["text"][:80].replace("\n", " ")
    print(f"[{section_id}] {preview}")