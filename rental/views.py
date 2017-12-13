from django.shortcuts import render,HttpResponse
from .forms import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):

    title='Welcome|House Hub'

    return render(request,'index.html',{'title':title})



@login_required(login_url='/accounts/login/')
def choice(request):
    current_user = request.user.id
    print(current_user)
    current_using=request.user    
    length_list=Landlord_tenant.objects.filter(user_id=current_user)

    x=Landlord_tenant.objects.get(user=1).choice
    print(x)
    if (Landlord_tenant.objects.get(user=1).choice)==1 and (Landlord_tenant.objects.filter(user_id=current_user).exists())!=False:
       return redirect(landlord)


    elif (Landlord_tenant.objects.get(user=1).choice)==2 and (Landlord_tenant.objects.filter(user_id=current_user).exists())!=False:
        return redirect(user_index)


    else:
        title='Tenant| Landlord'
        return render(request,'choose.html',{'title':title})




@login_required(login_url='/accounts/login/')
def landlord_prof(request):
    current_user = request.user.id
    print(current_user)
    current_using=request.user    
    length_list=Landlord_tenant.objects.filter(user_id=current_user)

    x=Landlord_tenant.objects.get(user=1).choice
    print(x)
    if (Landlord_tenant.objects.get(user=1).choice)==1 and (Landlord_tenant.objects.filter(user_id=current_user).exists())!=False:

         title='Name'
        form=HouseForm()
        return render(request,'landlord/profile.html',{'title':title,'form':form})


    elif (Landlord_tenant.objects.get(user=1).choice)==2 and (Landlord_tenant.objects.filter(user_id=current_user).exists())!=False:
        return redirect(user_index)
       
    else:
        return redirect(choice)
   


@login_required(login_url='/accounts/login/')

def user_index(request):
    current_user = request.user.id
    print(current_user)
    current_using=request.user    
    length_list=Landlord_tenant.objects.filter(user_id=current_user)

    x=Landlord_tenant.objects.get(user=1).choice
    print(x)
    if (Landlord_tenant.objects.get(user=1).choice)==1 and (Landlord_tenant.objects.filter(user_id=current_user).exists())!=False:

        return redirect(landlord_prof)

    elif (Landlord_tenant.objects.get(user=1).choice)==2 and (Landlord_tenant.objects.filter(user_id=current_user).exists())!=False:
        
        title='Name'
        form=HouseForm()
        return render(request,'tenant/profile.html',{'title':title,'form':form})

    else:
        return redirect(choice)
   


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


