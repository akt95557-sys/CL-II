# Collection of documents
documents = {
    "Doc1": "heart disease patient health",
    "Doc2": "disease treatment patient doctor",
    "Doc3": "heart health doctor lifestyle"
}

# 1. Build Inverted Index (Term -> Set of Doc IDs)
inverted_index = {}
for doc_id, text in documents.items():
    for word in text.lower().split():
        inverted_index.setdefault(word, set()).add(doc_id)

# Print Inverted Index
print("--- INVERTED INDEX ---")
for word, doc_ids in sorted(inverted_index.items()):
    print(f"{word} -> {sorted(list(doc_ids))}")

# 2. Document Retrieval (Query: "heart disease")
query = "heart disease".lower().split()
##query = input("\nEnter search query: ").lower().split()
results = set(documents.keys())

for word in query:
    results = results.intersection(inverted_index.get(word, set()))

print(f"\nRetrieved Documents for '{' '.join(query)}':", sorted(list(results)))