from django.shortcuts import render
from .forms import contactForm, StudentData,passwordValidation
# Create your views here.


def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request, 'about.html')


def form(request):
    return render(request, 'forms.html')


def Django_forms(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
        return render(request, 'django_forms.html', {'form': form})
    else:
        form = contactForm()
    return render(request, 'django_forms.html', {'form': form})


# def student_forms(request):
#     if request.method == 'POST':
#         form = StudentData(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:
#         form = StudentData()
#     return render(request, 'django_forms.html', {'form': form})

def password(request):
    if request.method == 'POST':
        form = passwordValidation(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = passwordValidation()
    return render(request, 'django_forms.html', {'form': form})