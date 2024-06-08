from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from scraper.utils import CoinMarketCapScraper
import uuid

job_id = None
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
        scraper = CoinMarketCapScraper()
        coin_data = scraper.get_coin_data(coin_name)
        # job_id = str(uuid.uuid4())
        print(job_id) 
        print(type(job_id))
        data = {'job_id' : job_id,'tasks': [{'coin': coin_data['coin'], 'output': coin_data}]} 
        # print(data)
        

        return render(request, 'scraper/results.html', {'data': data})   
    else:  
        return HttpResponse("Method not allowed", status=405)


def generate_job_id(request):
    global job_id
    if job_id:
        return HttpResponse(job_id)
    else: 
        job_id = str(uuid.uuid4())
        return HttpResponse(job_id)


def final_result(request):

    return render(request, 'scraper/results.html', {'data': data})   

    



