import requests
from bs4 import BeautifulSoup
import sys

urls = [
    "https://www.formula1.com/en/results/2021/races",
    "https://www.formula1.com/en/results/2022/races",
    "https://www.formula1.com/en/results/2023/races",
    "https://www.formula1.com/en/results/2024/races",
    "https://www.formula1.com/en/results/205/races"
]

def check_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises error if HTTP status is 4xx or 5xx
    except Exception as e:
        print(f"ERROR: Could not reach {url}: {e}")
        return False

    # Parse HTML and check for table
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if not table:
        print(f"ERROR: No table found on {url}")
        return False

    print(f"{url} is up and contains a table.")
    return True

for url in urls:
    if not check_website(url):
        sys.exit(1)  # Exit immediately on failure

print("All websites are reachable and contain a table.")
sys.exit(0)
