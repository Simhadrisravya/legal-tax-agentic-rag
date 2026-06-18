import re

def split_income_tax_sections(text):
    body_start_marker = "This Act may be called the Income-tax Act, 1961"
    idx = text.find(body_start_marker)
    if idx != -1:
        line_start = text.rfind("\n", 0, idx)
        text = text[line_start:] if line_start != -1 else text[idx:]

    pattern = r"\n\s*(?:\d{1,2}\[|\[)?(\d+[A-Z-]*)\.\s"
    matches = list(re.finditer(pattern, text))

    footnote_signal = re.compile(
        r"w\.e\.f\.|\bibid\b|\bAct\s+\d+\s+of\s+\d{4}\b|Amendment\)?\s+Act"
    )

    def line_text(m):
        end = text.find("\n", m.end())
        return text[m.start():end if end != -1 else len(text)]

    real_matches = []
    for m in matches:
        number = m.group(1)
        if re.fullmatch(r"\d{4}", number):
            continue
        if footnote_signal.search(line_text(m)):
            continue
        real_matches.append(m)

    sections = []
    for i, m in enumerate(real_matches):
        start = m.start()
        end = real_matches[i + 1].start() if i < len(real_matches) - 1 else len(text)
        sections.append({"section": m.group(1), "text": text[start:end]})

    return sections

