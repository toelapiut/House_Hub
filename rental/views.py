from django.shortcuts import render

# Create your views here.
def index(request):

    title='Welcome|House Hub'

    return render(request,'index.html',{'title':title})