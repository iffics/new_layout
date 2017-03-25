from django.shortcuts import render, get_object_or_404, redirect,Http404
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, ShopsForm, ReviewsForm
from .models import Shops, Reviews
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


"""----------User Registration View----------"""
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request, 'assets/pages/new/index.html')
    return render(request, 'assets/pages/register.html', {'form': form})

"""----------End Of User Registration View----------"""


"""----------User Logout View----------"""

def logout_user(request):
    logout(request)
    return render(request, 'assets/pages/new/index.html')

"""---------- End of User Logout View ----------"""


"""---------- User Login View ----------"""

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'assets/pages/new/index.html')
            else:
                return render(request, 'assets/pages/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'assets/pages/login.html', {'error_message': 'Invalid login'})

    return render(request, 'assets/pages/login.html')

"""---------- End of User Login View ----------"""



"""---------- Shop-Registration-View ----------"""

def srv(request):
    form = ShopsForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.user= request.user
        form.save()
        return redirect('my_crs.views.s_detail')  # HttpResponse('form submitted')
    return render(request, 'assets/pages/shopform.html', {'form': form})

"""---------- End-Of-Shop-Registration-View ----------"""


"""---------- Review-Registration-View ----------"""

def re_form(request):
    form = ReviewsForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        print('done')
        return redirect('my_crs.views.s_detail')  # HttpResponse('form submitted')
    return render(request, 'assets/pages/rform.html', {'form': form})

"""---------- End-Of-Review-Registration-View ----------"""


"""---------- Home-Page-View ----------"""

def home(request):
    data_list = Shops.objects.all()
    query=request.GET.get('q')
    if query:
        data_list = data_list.filter(comment__icontains=query)
    return render(request, 'assets/pages/new/index.html')

"""---------- End-Of-Home-Page-View ----------"""








def s_detail(request):
    data_list = Shops.objects.all()

    query=request.GET.get('q')
    if query:
        data_list = data_list.filter(name__icontains=query)
    paginator = Paginator(data_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
    context = {
        'data':data,
    }
    # queryset_list = Shops.objects.all()
    # query = request.GET.get("q")
    # if query:
    #      queryset_list = queryset_list.filter(name__icontains=query)
    #     #return render(request, 'assets/pages/sd.html', {'data': data, 'query': query})

    return render(request, 'assets/pages/sd.html', context)







def single_shop(request, id=None):
    instance = get_object_or_404(Shops, id=id)
    # review = Reviews.objects.all()

    # data = Shops.objects.all()
    context = {

        'title': instance.name,
        'instance': instance,

    }

    return render(request, 'assets/pages/detail_of_sig_shop.html', context)

# def edit_data(request, id=None):
#
#     instance = get_object_or_404(Shops, id=id)
#
#     form = ShopsForm(request.POST or None,instance=instance)
#     if form.is_valid():
#         form = form.save(commit=True)
#
#     context = {
#
#         'title': instance.name,
#         'instance': instance,
#         'form': form,
#     }
#     delete_post(request,id=id)
#     return render(request, 'assets/pages/shopform.html', context)
#







def edit_data(request, id=None):

    instance = get_object_or_404(Shops, id=id)

    if instance.user == request.user:

        form = ShopsForm(request.POST or None,instance=instance)
        context = {'title': instance.name,'instance': instance,'form': form,}

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return render(request,'assets/pages/detail_of_sig_shop.html',{'instance':instance})
    else:
        raise Http404
    return render(request, 'assets/pages/shopform.html', context)












def delete_post(request,id=None):
    instance = get_object_or_404(Shops,id=id)
    if instance.user == request.user:
        instance.delete()
    else:
        raise Http404
    return render(request,'assets/pages/sd.html')











def revs(request):
    review_list = Reviews.objects.all()
    shp = Shops.objects.all()
    paginator = Paginator(review_list, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        review = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        review = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        review = paginator.page(paginator.num_pages)
    context = {
        'review':review,




    }
    return render(request, 'assets/pages/reviews.html', context)

# def one_p_r(request, id=None):
#     instance = get_object_or_404(Shops, pk=id)
#     # data = Shops.objects.all()
#     context = {
#         'title': instance.name,
#         'instance':instance
#     }
#     return render(request,'assets/pages/sd.html',context)


def ser(request):

    return  render(request,'assets/pages/sd.html')