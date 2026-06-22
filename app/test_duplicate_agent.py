from duplicate_agent import find_duplicates

stores = [
    {"store_name": "Downtown Chicago"},
    {"store_name": "Downtown Chicago 2"},
    {"store_name": "Miami Beach"}
]

duplicates = find_duplicates(stores)

print(duplicates)