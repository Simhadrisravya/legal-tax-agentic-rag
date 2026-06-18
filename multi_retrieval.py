from section_search import get_section


def multi_retrieve(document, sections):

    contexts = []

    for section in sections:

        data = get_section(
            document,
            section
        )

        if data:

            contexts.append(
                data["text"]
            )

    return "\n\n".join(contexts)