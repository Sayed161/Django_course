from django.http import HttpResponse

def Home(request):
   return HttpResponse("THis is Home Page")
def contact (request):
   return HttpResponse("This is a contact page")
