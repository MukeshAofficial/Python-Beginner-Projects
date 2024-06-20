import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# URL of the page to scrape
url = "https://internshala.com/jobs/data-science-jobs/"
req = requests.get(url)
soup = bs(req.content, 'html.parser')

# Scrape data
jobs_data = []
for job in soup.find_all('div', class_='individual_internship'):
    title = job.find('h3', class_='job-internship-name').text.strip() if job.find('h3', class_='job-internship-name') else 'N/A'
    
    location_tag = job.find('p', class_='locations')
    if location_tag:
        location = location_tag.find('a').get_text(strip=True)
    
    experience_tag = job.find('div', class_='item_body desktop-text')
    experience = experience_tag.text.strip() if experience_tag else 'N/A'
    
    salary_tag = job.find('span', class_='desktop')
    salary = salary_tag.text.strip() if salary_tag else 'N/A'
    
    jobs_data.append({
        'Title': title,
        'Location': location,
        'Experience': experience,
        'Salary': salary
    })

# Create DataFrame
df = pd.DataFrame(jobs_data)


df.to_csv('internshala_data_science_jobs.csv', index=False)

