
from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def account(request):
    fulltext= request.GET['fulltext']
    return render(request,'account.html',{'fulltext':fulltext})
def about(request):
    return render(request,'about.html')