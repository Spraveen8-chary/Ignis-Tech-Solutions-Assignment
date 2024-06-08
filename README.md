# Ignis-Tech-Solutions-Assignment

## Assignment Problem Statement
Write a Django rest framework API that will take in a list of crypto coin acronyms, scrape the website data, and return the JSON response.

## Solution Analysis
### Objective
Developed a Django REST Framework API that accepts a list of cryptocurrency acronyms, scrapes data from a specified website, and returns the data in JSON format.

### Libraries used
- djangorestframework
- celery
- requests
- selenium
- uuid
- beautifulsoup
- json

### Benefits
- Scalability: Celery and BeautifulSoup allow the scraping tasks to run asynchronously, making the API scalable.
- Modularity: Each component (API, scraping, task management) is modular, making the system easy to maintain and extend.

### URL Allotted for Scraping Data
```https://coinmarketcap.com/```

![Screenshot (347)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/9c7948ff-28a2-470c-a05b-a5a7220c92cf)

- Data to be Scraped.

![Screenshot 2024-06-08 151708](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/3ffd5756-3ef6-4e16-aa9b-e737ac1d7544)

![Screenshot 2024-06-08 152145](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/d125afec-8a19-47a6-aab7-490bb63ae2b2)

## Functionality Overview
- ```http://127.0.0.1:8000/api/taskmanager/start_scraping/```: A homepage to take input of coins that are to be retrieved.
  
- ```http://127.0.0.1:8000/api/taskmanager/scraping_status/```: A page where responses are collected from the backend.
  
- ```http://127.0.0.1:8000/api/taskmanager/start_scraping/< job_id >/```: A final page where the result is displayed along with job_id in the URL, the response is showcased in tabular format to understand easily and in the bottom complete JSON response is printed.
  
- ```terminal```: In the terminal actual JSON required output is printed you can observe them in the output section.

## Execution Procedure
- Initially clone the git repo ```https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/```
- Extract the zip folder of your project folder.
- Open the ```command prompt``` at crypto_scraper folder and download the required libraries using this command ```pip install -r requirements.txt```
- After downloading all the dependencies simply type this command ```python manage.py migrate```
- Now we'll run our application using this command for running the application ```python manage.py runserver```
- It returns the ```http://127.0.0.1:8000``` in your terminal, copy that and paste it into the browser.
- Now some welcome text will be shown ignore it and type ```http://127.0.0.1:8000/api/taskmanager/start_scraping/``` in the url it will be navigated to the input page.
- Now give the input of coin name separated by a comma (,) Example: bitcoin, notcoin, duko
- Then after submitting the coin name it will be redirected to the final page.

## OUTPUT

- Coin Input Page

![Screenshot (336)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/704ff3b2-232f-41f4-9624-0b73837d1ccf)

- Final response page in tabular form
  
![Screenshot (338)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/8dda33d3-d8dd-4434-916d-6c53c24a5828)

![Screenshot (339)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/dab38c1d-f631-4738-9978-0088624e3444)

![Screenshot (340)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/2e7a1663-35a5-46e2-b2a0-3b8eceabe952)

![Screenshot (341)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/1eb4c8e2-1eb6-4f82-955d-5cc7c40e82e2)

- JOSN response in required form along with job_id
  
![Screenshot (342)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/484ff9e9-6f03-4d31-b7c8-74e69abbac87)

## Terminal OUTPUT
- JSON response
  
![Screenshot (343)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/dbadc57c-1e0e-41e3-a391-953e87b334d4)

![Screenshot (344)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/9b2decf6-e908-43e5-93e1-57c34a418a00)

![Screenshot (345)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/945152f5-da00-4d16-aedc-c8332357e869)

![Screenshot (346)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/f8792fb4-933a-46a5-89a1-f67413a94b72)
