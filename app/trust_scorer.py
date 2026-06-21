import pandas as pd

stores = pd.read_csv("sample-data/stores.csv")

for index, row in stores.iterrows():

    score = 100
    issues = []

    # Missing ZIP code
    if pd.isna(row["zip code"]):
        score -= 20
        issues.append("Missing ZIP code")

    # Missing franchise owner
    if pd.isna(row["franchise_owner"]):
        score -= 20
        issues.append("Missing franchise owner")

    # Missing region
    if pd.isna(row["Region"]):
        score -= 15
        issues.append("Missing region")

    # Invalid menu board count
    menu_boards = str(row["# Menu Boards"]).strip().lower()

    if not menu_boards.isdigit():
        score -= 20
        issues.append(f"Invalid menu board count: {row['# Menu Boards']}")

    # Confidence classification
    if score >= 90:
        confidence = "HIGH"
    elif score >= 70:
        confidence = "MEDIUM"
    else:
        confidence = "LOW"

    print("=" * 50)
    print(f"Store: {row['Store Name']}")
    print(f"Store ID: {row['store_id']}")
    print(f"Confidence: {confidence}")
    print(f"Score: {score}")

    if issues:
        print("\nIssues Found:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("\nNo issues detected.")