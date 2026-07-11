from itertools import combinations

# ===========================================================
# MOVIE RECOMMENDATION (Rule-Based)
# ===========================================================
users = [
    {"name": "Rahul", "watched": ["Action", "SciFi"]},
    {"name": "Anita", "watched": ["Romance", "Drama"]},
    {"name": "Riya", "watched": ["Action", "Comedy"]}
]

movie_rules = {
    "Action": "John Wick",
    "SciFi": "Inception",
    "Romance": "The Notebook",
    "Drama": "Taare Zameen Par",
    "Comedy": "Superbad"
}

print("========== MOVIE RECOMMENDATION ==========")

# 1. Search User & Recommend Movie
name = input("Enter user name: ")
found = False
for user in users:
    if user["name"].lower() == name.lower():
        found = True
        print("\nUser Name :", user["name"])
        print("Watched Genres :", ", ".join(user["watched"]))
        print("\nRecommended Movies:")
        for genre in user["watched"]:
            if genre in movie_rules:
                print(f"{genre} --> {movie_rules[genre]}")
if not found:
    print("User not found!")

# 2. Count Users who watched Action
count = 0
for user in users:
    if "Action" in user["watched"]:
        count += 1
print("\nUsers who watched Action:", count)

# 3. Find Most Common Genre
genre_count = {}
for user in users:
    for genre in user["watched"]:
        genre_count[genre] = genre_count.get(genre, 0) + 1

max_genre = ""
max_count = 0
for genre, cnt in genre_count.items():
    if cnt > max_count:
        max_count = cnt
        max_genre = genre

print("Most Common Genre:", max_genre)
print("Occurred:", max_count, "times")


# ===========================================================
# 4. CUSTOMER SEGMENTATION
# ===========================================================
customers = [
    {"name": "Rahul", "total_spent": 15000},
    {"name": "Anita", "total_spent": 3000},
    {"name": "Riya", "total_spent": 8000}
]

print("\n========== CUSTOMER SEGMENTATION ==========")
for customer in customers:
    if customer["total_spent"] > 10000:
        segment = "High Value"
    elif customer["total_spent"] > 5000:
        segment = "Medium Value"
    else:
        segment = "Low Value"
    print(customer["name"], "->", segment)


# ===========================================================
# 5. PRODUCT RECOMMENDATION
# ===========================================================
products_bought = {
    "Rahul": ["Laptop", "Mouse"],
    "Anita": ["Mobile", "Charger"],
    "Riya": ["Laptop", "Keyboard"]
}

print("\n========== PRODUCT RECOMMENDATION ==========")
for user1 in products_bought:
    for user2 in products_bought:
        if user1 != user2:
            common = set(products_bought[user1]) & set(products_bought[user2])
            if common:
                recommend = set(products_bought[user2]) - set(products_bought[user1])
                if recommend:
                    print(f"Recommend to {user1}: {recommend} (both bought {common})")


# ===========================================================
# 6. MARKET BASKET ANALYSIS
# ===========================================================
transactions = [
    ["Bread", "Butter", "Milk"],
    ["Bread", "Butter"],
    ["Milk", "Eggs"],
    ["Bread", "Milk"]
]

pair_count = {}
for transaction in transactions:
    for pair in combinations(sorted(transaction), 2):
        pair_count[pair] = pair_count.get(pair, 0) + 1

most_common_pair = max(pair_count, key=pair_count.get)
print("\n========== MARKET BASKET ANALYSIS ==========")
print("Most frequently bought together:", most_common_pair, "->", pair_count[most_common_pair], "times")


# ===========================================================
# 7. FRAUD DETECTION (Pattern Discovery)
# ===========================================================
transactions_amount = {
    "Rahul": [200, 250, 220, 5000],
    "Anita": [100, 120, 110]
}

print("\n========== FRAUD DETECTION ==========")
for user, amounts in transactions_amount.items():
    avg = sum(amounts) / len(amounts)
    for amt in amounts:
        if amt > avg * 3:
            print(f"Possible Fraud: {user} spent {amt} (avg is {avg:.2f})")
