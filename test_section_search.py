from section_search import get_section

result = get_section(
    "GST_ACT.pdf",
    "29"
)

if result:
    print("FOUND SECTION")
    print(result["section"])
    print(result["text"][:1000])
else:
    print("NOT FOUND")
