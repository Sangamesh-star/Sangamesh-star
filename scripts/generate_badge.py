import requests
from datetime import datetime

username = "Sangamesh-star"
max_score = 1000
grade = "?"
color = "#999"
today = datetime.now().strftime("%Y-%m-%d")

response = requests.get(f"https://api.github.com/users/{username}")
data = response.json()
repos = data.get("public_repos", 0)
followers = data.get("followers", 0)

score = repos * 5 + followers * 2
percent = min((score / max_score) * 100, 100)
percent_str = f"{percent:.1f}"

if percent >= 90:
    grade = "A+"
    color = "#4CAF50"
elif percent >= 80:
    grade = "B+"
    color = "#2196F3"
elif percent >= 70:
    grade = "B"
    color = "#FFC107"
elif percent >= 60:
    grade = "C+"
    color = "#FF9800"
else:
    grade = "C"
    color = "#F44336"

radius = 70
circumference = 2 * 3.1416 * radius
offset = circumference * (1 - percent / 100)

svg = f'''<svg width="160" height="160" viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
  <circle cx="80" cy="80" r="{radius}" stroke="#eee" stroke-width="12" fill="none" />
  <circle
    cx="80"
    cy="80"
    r="{radius}"
    stroke="{color}"
    stroke-width="12"
    fill="none"
    stroke-dasharray="{circumference:.1f}"
    stroke-dashoffset="{offset:.1f}"
    stroke-linecap="round"
    transform="rotate(-90 80 80)"
  />
  <text x="50%" y="52%" text-anchor="middle" font-size="36" font-weight="bold" fill="{color}">{grade}</text>
  <text x="50%" y="72%" text-anchor="middle" font-size="14" fill="#555">{percent_str}%</text>
  <text x="50%" y="88%" text-anchor="middle" font-size="12" fill="#888">GitHub Grade • {today}</text>
</svg>'''

with open("grade-badge.svg", "w") as f:
    f.write(svg)
