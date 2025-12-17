import requests
import csv

# Replace with your GitHub username and personal access token
USERNAME = "kreier"
TOKEN = "YOUR_TOKEN_HERE"

# Base URL for GitHub API
BASE_URL = f"https://api.github.com/users/{USERNAME}/repos"

# Headers for authentication
headers = {"Authorization": f"token {TOKEN}"}

repos_data = []
page = 1

while True:
    # Paginate through repositories
    url = f"{BASE_URL}?per_page=100&page={page}"
    response = requests.get(url, headers=headers)
    repos = response.json()

    if not repos or response.status_code != 200:
        break

    for repo in repos:
        name = repo["name"]
        url = repo["html_url"]

        # Fetch language breakdown for each repo
        lang_url = repo["languages_url"]
        lang_response = requests.get(lang_url, headers=headers)
        lang_data = lang_response.json()

        # Find the main language (largest size)
        if lang_data:
            main_language = max(lang_data, key=lang_data.get)
            size = lang_data[main_language]
        else:
            main_language = None
            size = 0

        repos_data.append([name, url, main_language, size])

    page += 1

# Write to CSV
with open("repositories.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "URL", "Main Language", "Size"])
    writer.writerows(repos_data)

print("Export complete! Saved to repositories.csv")
