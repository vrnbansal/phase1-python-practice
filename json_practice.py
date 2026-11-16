import json

result = {
    "score": 3,
    "total": 5,
    "wrong": ["3 x 4", "5 x 6"]
}

with open("results.json", "w") as file:
    json.dump(result, file, indent=2)

print("Saved to results.json")

with open("results.json", "r") as file:
    loaded = json.load(file)

print("Score:", loaded["score"], "out of", loaded["total"])
print("Questions to practise:", loaded["wrong"])