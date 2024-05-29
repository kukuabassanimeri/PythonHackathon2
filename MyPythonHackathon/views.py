from django.shortcuts import render
import requests
import random

def python(request):
    # Fetch random fact
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    data = response.json()
    fact = data['text']
    
    # Fetch student data
    try:
        response = requests.get('https://freetestapi.com/api/v1/students')
        response.raise_for_status()  
        data = response.json()
        
        if data:
            student = random.choice(data)  
            name = student.get('name')
        else:
            name = "No student found"
    except requests.RequestException as e:
        name = "Failed to fetch data"
    
    # Fetch activity data
    try:
        response1 = requests.get('https://www.boredapi.com/api/activity')
        response1.raise_for_status()
        data3 = response1.json()
        act = data3['activity']
    except requests.RequestException as e:
        act = "Failed to fetch activity"
    
    # Fetch dog image
    try:
        histo = requests.get('https://dog.ceo/api/breeds/image/random')
        histo.raise_for_status()
        year = histo.json()
        event = year['message']
    except requests.RequestException as e:
        event = "Failed to fetch image"
    
    return render(request, 'python.html', {'fact': fact, 'name': name, 'act': act, 'event': event})


# django.shortcuts import render
# import requests
# import random
# # Create your views here.


# def python(request):
#     response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
#     data = response.json()
#     fact = data['text']
    
#     try:
#         response = requests.get('https://freetestapi.com/api/v1/students')
#         response.raise_for_status()  
#         data = response.json()
        
#         if data:
#             student = random.choice(data)  
#             name = student.get('name')
            
#         else:
#             name = "No student found"

#     except requests.RequestException as e:
#         name = "Failed to fetch data"
    
    
#     response1 = requests.get('https://www.boredapi.com/api/activity')
#     data3 = response1.json()
#     act = data3['activity']
    
#     histo = requests.get('https://dog.ceo/api/breeds/image/random')
#     year = histo.json()
#     event = year['message']
    
#     return render(request, 'python.html', {'fact': fact, 'name': name, 'act': act, 'event': event})