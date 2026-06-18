def get_document(query):

    query = query.lower()

    if "gst" in query:
        return "GST_ACT.pdf"

    elif "gst rules" in query:
        return "GST_Rules.pdf"

    elif "income tax" in query:
        return "Income_Tax_Act.pdf"

    return None