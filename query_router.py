import re

SECTION_PATTERN = re.compile(r"section\s+(\d+[a-zA-Z]{0,3})", re.IGNORECASE)

INCOME_TAX_KEYWORDS = [
    "80c", "80d", "income tax", "salary", "deduction", "tds", "itr",
    "assessment year", "capital gains", "house property", "exemptions"
]

GST_KEYWORDS = [
    "gst", "cgst", "sgst", "igst", "input tax credit", "itc", "supply",
    "invoice", "reverse charge", "rcm", "composition scheme",
    "registration", "cancellation", "revocation"
]


def classify_document(q_lower, section_number=None):
    has_letters = bool(section_number) and bool(re.search(r"[A-Z]", section_number, re.IGNORECASE))
    if any(k in q_lower for k in INCOME_TAX_KEYWORDS) or has_letters:
        return "Income_Tax_Act.pdf"
    if any(k in q_lower for k in GST_KEYWORDS):
        return "GST_ACT.pdf"
    return None


def route_query(question_text):
    result = {"document": None, "section": None, "sections": None}

    if not question_text:
        return result

    q_lower = question_text.lower()
    raw_matches = SECTION_PATTERN.findall(question_text)

    section_numbers = []
    seen = set()
    for raw in raw_matches:
        num = raw.upper()
        if num not in seen:
            seen.add(num)
            section_numbers.append(num)

    if len(section_numbers) >= 2:
        result["document"] = classify_document(q_lower, section_numbers[0])
        result["sections"] = section_numbers
        return result

    if len(section_numbers) == 1:
        result["document"] = classify_document(q_lower, section_numbers[0])
        result["section"] = section_numbers[0]
        return result

    result["document"] = classify_document(q_lower)
    return result


auto_route_document = route_query
