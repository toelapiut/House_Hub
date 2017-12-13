from django.shortcuts import render
from .forms import *
# Create your views here.
def index(request):

    title='Welcome|House Hub'

    return render(request,'index.html',{'title':title})

def choice(request):

    title='LandLord|Tenant'

    return render(request,'index.html',{'title':title})



def landlord_prof(request):

    title='username'

    form=HouseForm()


    return render(request,'landlord/profile.html',{'title':title,'form':form})