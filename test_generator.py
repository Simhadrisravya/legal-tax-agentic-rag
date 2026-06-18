from ingestion.generator import generate_answer

context = [
    "GST means Goods and Services Tax.",
    "GST was introduced in India in 2017."
]

question = "What is GST?"

answer = generate_answer(question, context)

print(answer)