from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def events(request):
    return render(request,'events.html')

def gallery(request):
    return render(request,'gallery.html')

def reports(request):
    return render(request,'reports.html')

def news(request):
    return render(request,'news.html')

def volunteers(request):
    return render(request,'volunteers.html')

def downloads(request):
    return render(request,'downloads.html')

def contact(request):
    return render(request,'contact.html')