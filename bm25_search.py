from rank_bm25 import BM25Okapi


def create_bm25(chunks):

    tokenized_chunks = [
        chunk.split()
        for chunk in chunks
    ]

    bm25 = BM25Okapi(
        tokenized_chunks
    )

    return bm25


def bm25_search(
    query,
    bm25,
    chunks,
    top_k=3
):

    tokenized_query = query.split()

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )

    results = [
        chunks[i]
        for i in ranked[:top_k]
    ]

    return results