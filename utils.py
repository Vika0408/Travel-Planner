import requests
from bs4 import BeautifulSoup

def fetch_top_activities(destination):
    url = f"https://www.google.com/search?q=best+things+to+do+in+{destination.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    activities = []
    for item in soup.select("h3"):  # Adjust as per Google's structure
        activities.append(item.text)
    
    return activities[:5]  # Return top 5 activities
