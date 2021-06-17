import requests
import pandas as pd

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "referer": "https://www.udemy.com/courses/search/?src=ukw&q=python"
}

total_courses = []

for i in range(1, 5):
    url_api = "https://www.udemy.com/api-2.0/search-courses/?src=ukw&q=python&skip_price=true&p=" + str(i)

    response = requests.get(url_api, headers=headers)

    data = response.json()

    courses = data['courses']

    for course in courses:
        title = course['title']
        num_reviews = course['num_reviews']
        rating = course['rating']
        total_courses.append(
            {
                "title": course['title'],
                "num_reviews": course['num_reviews'],
                "rating": course['rating']
            }
        )

df = pd.DataFrame(total_courses)
print(df)
df.to_csv("udemy_courses.csv")