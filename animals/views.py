from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
# from django.http import HttpResponse
# from livestock import settings
# from django.core.mail import EmailMessage, send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render
from .forms import UploadFileForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from .forms import ProfileForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *
# import magic
# import python_magic

from django.conf import settings

# Create your views here.
videos = Video.objects.all()



def welcome(request):
    videos = Video.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        videos = videos.filter(title__icontains=search_query)
    return render(request, "animals/welcome.html", {'videos': videos})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home/')
    else:
        form = UserCreationForm()
    return render(request, 'animals/signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
      user = request.POST['username']
      request.session['user']=user
      pas = request.POST['password']
      user = authenticate(request, username=user, password=pas)

      if user is not None:
          login(request, user)
          return redirect('/home')
      else:
          messages.error(request, "INVALID CREDENTIALS")
          return redirect('/login')
    return render(request, "animals/login.html")


@login_required(login_url='login')
def home(request):
    data = stock.objects.all()
    context = {"data": data}
    
    return render(request, "animals/home.html", context)


def add(request):
    if request.method == "POST":
        aid = request.POST['aid']
        aclass = request.POST['aclass']
        sex = request.POST['sex']
        weight = request.POST['weight']
        insurance = request.POST['insurance']
        vstatus = request.POST['vstatus']
        vdate = request.POST['vdate']
        ddate = request.POST['ddate']
        newstock = stock(id=aid, aclass=aclass, sex=sex, weight=weight, insurance=insurance, vacstatus=vstatus, vdate=vdate, ddate=ddate)
        newstock.save()
        return redirect('/home')
    return render(request, "animals/add.html")
    

def edit(request, id):
    obj = stock.objects.get(id=id)
    context = {"obj": obj}
    return render(request, "animals/edit.html", context)

def logout_view(request):
    logout(request)
    return redirect('/')

# def delete_view(request, id):
#     obj = stock.objects.get(id=id)
#     obj.delete()
#     data = stock.objects.all()
#     context = {"data": data}
#     return redirect('', context)

def delete_view(request, id):
    obj = get_object_or_404(stock, id=id)
    obj.delete()
    return redirect('home')

@ensure_csrf_cookie
def upload_display_video(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            #print(file.name)
            handle_uploaded_file(file)
            return render(request, "animals/upload_display_video.html", {'filename': file.name})
    else:
        form = UploadFileForm()
        return redirect('/home')
    return render(request, 'animals/upload_display_video.html', {'form': form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# def profile(request):
#     form =User.objects.filter(username=request.session['user_name'])
#     if request.method == 'POST':
#         form = User.objects.filter(username=request.session['user_name'])
#         if form.is_valid():
#             form.save()
#             return redirect('/home')  # You can change 'profile' to the URL name of your profile view
#     else:
#         form = ProfileForm(instance=request.user.profile)
#     return render(request, 'animals/profile1.html', {'form': form})

from django.contrib.auth.models import User
from .models import Profile

def profile(request):
    userdata = str(request.session['user'])
    try:
        user = User.objects.get(username=userdata)
        try:
            profiles = Profile.objects.get(user=user)
            return render(request, 'animals/profile.html', {'profile': profiles, 'user': user})
        except Profile.DoesNotExist:
            return redirect('/login')
    except User.DoesNotExist:
        return redirect('/login')

################################### video ####################################

def upload_video(request):
    videos = Video.objects.all()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'animals/video_upload.html', {'form': form})
    else:
        form = VideoForm()
    return render(request, 'animals/video_upload.html', {'form': form, 'videos': videos})

# def video_list(request):
#     videos = Video.objects.all()
#     return render(request, 'animals/videos_list.html', {'videos': videos})





# def video_detail(request, video_id):
#     video = get_object_or_404(Video, id=video_id)
#     related_videos = Video.objects.filter(tags__contains=video.tags).exclude(id=video_id)
#
#     # Determine the MIME type of the video file
#     mime = magic.Magic(mime=True)
#     video_mime_type = mime.from_file(video.video_file.path)
#
#     return render(request, 'animal/video_details.html',{'video': video, 'related_videos': related_videos, 'video_mime_type': video_mime_type})

def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    related_videos = Video.objects.filter(tags__contains=video.tags).exclude(id=video_id)

    return render(request, 'animals/video_details.html', {'video': video, 'related_videos': related_videos})




