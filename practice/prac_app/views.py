from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'prac_app/contact.html')

def about(request):
    return render(request, 'prac_app/about.html')