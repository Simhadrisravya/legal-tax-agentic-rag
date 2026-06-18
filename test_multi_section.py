from multi_section_search import get_sections

results = get_sections(
    "Income_Tax_Act.pdf",
    ["80C", "80D"]
)

print("Sections Found:", len(results))

for item in results:

    print()
    print("===================")
    print(item["section"])
    print("===================")

    print(
        item["text"][:500]
    )