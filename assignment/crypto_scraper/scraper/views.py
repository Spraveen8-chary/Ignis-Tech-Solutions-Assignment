from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.http import HttpResponse
from scraper.utils import CoinMarketCapScraper
import uuid
import json

job_id = str(uuid.uuid4())
data = {}

def index(request):
    return HttpResponse("Welcome to the API!")

def input_coin(request):
    
    return render(request, 'scraper/index.html')

def generate_job_id(request):
    global job_id
    job_id = str(uuid.uuid4())
    return HttpResponse(job_id)

def display_results(request):
    if request.method == 'POST':
        global data, job_id
        coin_name = request.POST.get('coin')
        coins = list(coin_name.split(','))
        scraper = CoinMarketCapScraper()
        all_data = scraper.get_multiple_coins_data(coins)
        job_id = str(uuid.uuid4())
        all_data['job_id'].append(job_id)
        data  = all_data 
        # print(data)
        data1 = json.dumps(data, indent=4)
        print(data1)
        return render(request, 'scraper/results.html', {'data': data })   
    else:  
        return HttpResponse("Method not allowed", status=405)
    

def generate_job_id(request):
    global job_id
    if job_id:
        return HttpResponse(job_id)
    else: 
        job_id = str(uuid.uuid4())
        return HttpResponse(job_id)


def final_result(request, job_id = job_id):

    return render(request, 'scraper/results.html', {'job_id' : job_id,'data': data})   


