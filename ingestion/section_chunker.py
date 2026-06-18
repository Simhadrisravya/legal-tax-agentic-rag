import re

def split_by_sections(text):


    pattern = r'\n\s*(\d+)\.\s*\n'

    matches = list(
        re.finditer(pattern, text)
    )

    sections = []

    for i in range(len(matches)):

        start = matches[i].start()

        if i < len(matches) - 1:
            end = matches[i + 1].start()
        else:
            end = len(text)

        chunk = text[start:end]

        section_number = matches[i].group(1)

        sections.append({
            "section": section_number,
            "text": chunk
        })

    return sections



