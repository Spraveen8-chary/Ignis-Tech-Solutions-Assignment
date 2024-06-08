# Ignis-Tech-Solutions-Assignment

# Assignment Problem Statement
Write a Django rest framework API that will take in a list of crypto coin acronyms, scrape the website data, and return the JSON response.

# Solution Analysis
## Objective
Developed a Django REST Framework API that accepts a list of cryptocurrency acronyms, scrapes data from a specified website, and returns the data in JSON format.

## Libraries used
- djangorestframework
- celery
- requests
- selenium
- uuid
- beautifulsoup
- json

## Benefits
- Scalability: Celery and BeautifulSoup allow the scraping tasks to run asynchronously, making the API scalable.
- Modularity: Each component (API, scraping, task management) is modular, making the system easy to maintain and extend.

## URL Allotted for Scraping Data
```https://coinmarketcap.com/```

![Screenshot (347)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/9c7948ff-28a2-470c-a05b-a5a7220c92cf)

from the above extracting below data

![Screenshot 2024-06-08 151708](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/3ffd5756-3ef6-4e16-aa9b-e737ac1d7544)

![Screenshot 2024-06-08 152145](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/d125afec-8a19-47a6-aab7-490bb63ae2b2)

![Screenshot (336)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/704ff3b2-232f-41f4-9624-0b73837d1ccf)

![Screenshot (338)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/8dda33d3-d8dd-4434-916d-6c53c24a5828)

![Screenshot (339)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/dab38c1d-f631-4738-9978-0088624e3444)

![Screenshot (340)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/2e7a1663-35a5-46e2-b2a0-3b8eceabe952)

![Screenshot (341)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/1eb4c8e2-1eb6-4f82-955d-5cc7c40e82e2)

![Screenshot (342)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/484ff9e9-6f03-4d31-b7c8-74e69abbac87)

![Screenshot (343)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/dbadc57c-1e0e-41e3-a391-953e87b334d4)

![Screenshot (344)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/9b2decf6-e908-43e5-93e1-57c34a418a00)

![Screenshot (345)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/945152f5-da00-4d16-aedc-c8332357e869)

![Screenshot (346)](https://github.com/Spraveen8-chary/Ignis-Tech-Solutions-Assignment/assets/108536707/f8792fb4-933a-46a5-89a1-f67413a94b72)
