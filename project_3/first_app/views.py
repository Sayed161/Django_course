from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'title': 'teacher', 'age': 30, 'course': [
        {"id": 1,
         "name": "Rahim",
         "fee": 12000},
        {"id": 2003,
         "name": "Karim",
         "fee": 10000},
        {"id": 903,
         "name": "jabbar",
         "fee": 15000},
    ]}
    return render(request, 'first_app/home.html',d)