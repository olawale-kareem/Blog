from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView


from .file import store_file
from .forms import FileForm
from .models import FileUploads


    

def index(request):
    return render(request, 'profiles/index.html')

class CreateProfileView(View):
    def get(self,request):
        form = FileForm()
        context = {'form': form}
        return render(request,'profiles/index.html', context)

    def post(self,request):
        submitted_form= FileForm(request.POST, request.FILES)
        context = {'form': submitted_form}
        if submitted_form.is_valid():
            # store_file(request.FILES['image']) # This manually stores into a file and this file cannot be querried
            file_uploaded = FileUploads.objects.create(image=request.FILES['image']) # This stores into a db for usage and retrieval
            file_uploaded.save()
            return HttpResponseRedirect('/profiles/')  # must us the same url path defined in the 'actions=' property of the form
        return render(request,'profiles/index.html', context)
    
# class CreateProfileView(CreateView):       # CreateView
#     template_name = 'profiles/index.html'
#     model = FileUploads
#     fields = '__all__'
#     success_url ='/profiles'

class ProfilesView(ListView):
    model = FileUploads
    template_name = 'profiles/user_profile.html'
    context_object_name = 'profiles'
