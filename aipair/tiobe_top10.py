import requests
from bs4 import BeautifulSoup

def fetch_tiobe_top10():
    url = "https://www.tiobe.com/tiobe-index/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    top10 = []
    if table:
        rows = table.find_all('tr')[1:11]  # Skip header, get top 10
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 6:
                name = cols[4].get_text(strip=True)
                rating = cols[5].get_text(strip=True)
                top10.append((name, rating))
    return top10

def display_top10():
    print("Top 10 Programming Languages (TIOBE Index):")
    for i, (name, rating) in enumerate(fetch_tiobe_top10(), 1):
        print(f"{i}. {name} - {rating}")

if __name__ == "__main__":
    display_top10()
