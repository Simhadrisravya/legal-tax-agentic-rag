from load_metadata import load_metadata

metadata = load_metadata()

def get_section(document_name, section_number):

    for item in metadata:

        if (
            item.get("document") == document_name
            and item.get("section") == section_number
        ):
            return item

    return None