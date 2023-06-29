from django.shortcuts import render
import requests
import json
import csv
import json
import os


def home(request):
    return render(request, "templates/index.html")

def about(request):
    return render(request, 'templates/about.html')

def contact(request):
    return render(request, 'templates/contact.html')

def service(request):
    return render(request, 'templates/service.html')

def work(request):
    url = os.environ['URL']
    response = requests.get(url)
    csvData = response.text
    # parse the CSV data as a list of dictionaries using the csv module
    csvReader = csv.DictReader(csvData.splitlines())
    jsonData = [row for row in csvReader]
    # convert the list of dictionaries to JSON format
    jsonString = json.dumps(jsonData)
    print(jsonString)
    return render(request, 'templates/work.html', context={"jsonString": jsonString})
