from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def service(request):
    return render(request, 'service.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def team(request):
    return render(request, 'team.html')
def portfolio(request):
    return render(request, 'portfolio.html')