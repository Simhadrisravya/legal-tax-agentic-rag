import re

def split_income_tax_sections(text):
    # Skip the Table of Contents at the front of the PDF. The TOC repeats every
    # section heading verbatim, so without this, every section gets double-counted.
    body_start_marker = "Short title, extent and commencement.—(1) This Act may be called"
    idx = text.find(body_start_marker)
    if idx != -1:
        line_start = text.rfind("\n", 0, idx)
        text = text[line_start:] if line_start != -1 else text[idx:]

    # The \[? makes a leading "[" optional — some sections (like 80C) are
    # printed with a bracket because they were substituted by a later amendment.
    print(type(footnote_signal))
    pattern = r'\n\s*\[?(\d+[A-Z-]*)\.\s'
    matches = list(re.finditer(pattern, text))

    # Amendment footnotes (printed at the bottom of nearly every page) match the
    # same "number + period" pattern as real section headers. They're reliably
    # identifiable because they always cite an amending Act and effective date.
    footnote_signal = re.compile(
        r'w\.e\.f\.|\bibid\b|\bAct\s+\d+\s+of\s+\d{4}\b|Amendment\)?\s+Act'
    )

    def line_text(m):
        end = text.find("\n", m.end())
        return text[m.start():end if end != -1 else len(text)]

    real_matches = []
    for m in matches:
        number = m.group(1)
        if re.fullmatch(r"\d{4}", number):   # plain 4-digit numbers are years, never real section numbers
            continue
        if footnote_signal.search(line_text(m)):
            continue
        real_matches.append(m)

    sections = []
    for i, m in enumerate(real_matches):
        start = m.start()
        end = real_matches[i + 1].start() if i < len(real_matches) - 1 else len(text)
        sections.append({
            "section": m.group(1),
            "text": text[start:end]
        })

    return sections