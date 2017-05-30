from django.shortcuts import render

#Home page all apps
def home(request):
    return render(request,'mysite/index.html')