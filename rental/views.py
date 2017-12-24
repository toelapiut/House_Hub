from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

# Create your views here.
def index(request):

    title='Welcome|House Hub'

    return render(request,'index.html',{'title':title})


@login_required(login_url='/accounts/login/')
def landlord_prof(request):


    current_user = request.user.id
    house=House.objects.filter(user=current_user)

    title='Name'



    if request.method == 'POST':

        post_form=HouseForm(request.POST,  request.FILES)

        if post_form.is_valid():
            print(post_form.data['house_name'])
            post_instance=House.objects.create(user=request.user,house_name=post_form.data['house_name'],landing_pic=post_form.files['landing_pic'])
            

            return render(request,'landlord/profile.html',{'title':title,'form':post_form})


    # else:


    post_form=HouseForm()
    return render(request,'landlord/profile.html',{'title':title,'form':post_form,'house':house})
        

def timeline(request):
    house=House.objects.all()


    return render(request,'time-line.html',{"house":house,})


@login_required(login_url='/accounts/login/')
@transaction.atomic
def update_landlord_profile(request):
    title='edit profile'
    user_id = request.user.id

    user_form = ProfileForm(request.POST, instance=request.user.profile, files=request.FILES)

    if request.method == 'POST':
    
        if user_form.is_valid():
            user_form.save()
            # print("user form is valid")

            return redirect(landlord_prof)
        else:
            print('invalid form') 
            # return redirect(landlord_prof)

    else:
        return render(request,'landlord/edit_profile.html',{'title':title,'form':user_form})


@csrf_exempt
def ajax_choice(request):
    current_user = request.user.id
    print(current_user)
    current_using=request.user
    
    length_list=Landlord_tenant.objects.filter(user_id=current_user)

    if (Landlord_tenant.objects.filter(user_id=current_user).exists())==False:
        # print(Landlord_tenant.objects.filter(user_id=current_user).exists()
        if request.POST.get('Tenant') != None:
            '''
            creates a Tenant instance once you click on the driver button Ajax
            '''
            Tenant = int(request.POST.get('Tenant'))
            tenant_instance=Landlord_tenant.objects.create(
                user=current_using, choice=Tenant)
            print(Tenant)
            data = {'success': 'You have been successfully Tenant'}

            return HttpResponse('HELLO')
            
            

        elif request.POST.get('Landlord') != None:

            '''
            creates a Landlord  instance once you click on the rider button Ajax
            '''

            print('yufshvjtkroyjophiugfeytdwrfetguhjkyfhdgsduf')

            Landlord = int(request.POST.get('LandLord'))
            landlord_instance = Landlord_tenant.objects.create(
                user=current_using, choice=Landlord)
            data = {'success': 'You have been successfully landlord'}

            return HttpResponse('HELLO')

        else:
             return HttpResponse('HELLO')

    else:
        print('hello')

        return HttpResponse('HELLO')





def add_house(request,id):


    current_user = request.user

    current_house = House.objects.get(id=id)

    house=House.objects.filter(id=id)

    room=Room.objects.filter(house=house)
    print(room)
    for i in room:
        print(i.room_pic.url)

    title='House'



    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid:

            comment = form.save(commit=False)

            comment.user = current_user

            comment.post = current_house

            comment.save()

            return redirect(add_house,current_house.id)

    else:

        form = CommentForm()

    if request.method == 'POST':
         
        room_form=RoomForm(request.POST, files=request.FILES)

        
    else:
        room_form=RoomForm()

    return render(request,'landlord/add_house.html', {"title":title,"form":form,"current_post":current_house,'house':house,'room':room})








@login_required(login_url='/accounts/register')
def like(request,id):

    current_user = request.user

    current_house = House.objects.get(id=id)

    like = Like(user=current_user,post=current_house,likes_number=1)

    like.save()

    return redirect(house_look,current_house.id)








def house_look(request,id):
    '''
    View function to display a single post, its comments and likes
    '''
    current_user = request.user
    try:
        current_house = House.objects.get(id=id)

        title = 'House Look'
        comments = Comment.get_post_comments(id)

        likes = Like.num_likes(id)

        like = Like.objects.filter(post=id).filter(user=current_user)

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'landlord/house_look.html', {"title":title, "post":current_post,"comments":comments,"likes":likes,"like":like })

