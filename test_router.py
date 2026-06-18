from query_router import route_query

print(
    route_query(
        "What are GST registration rules?"
    )
)

print(
    route_query(
        "What is Section 80C?"
    )
)

print(
    route_query(
        "Compare Section 80C and 80D"
    )
)
{
    'document': 'GST_ACT.pdf',
    'section': '22'
}

{
    'document': 'Income_Tax_Act.pdf',
    'section': '80C'
}

{
    'document': 'Income_Tax_Act.pdf',
    'sections': ['80C', '80D']
}