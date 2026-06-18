from section_search import get_section


def get_sections(document, section_numbers):
    found = []
    for section_number in section_numbers:
        data = get_section(document, section_number)
        if data:
            found.append(data)
    return found
