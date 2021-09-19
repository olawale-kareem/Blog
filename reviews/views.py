from django.shortcuts import render
from django.http import HttpResponseRedirect

# views
from django.views import View   # base view
from django.views.generic import ListView, DetailView #list and detail view
from django.views.generic.base import TemplateView  # Template view
from django.views.generic.edit import FormView, CreateView

# forms and models
from .forms import ReviewForm
from .models import Reviews





# generic or functional view
def reviews(request):
    # using modal form type
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save() # you can only save like this when you use the ModelForm
            return HttpResponseRedirect('thanks/')

    form = ReviewForm()
    context = {'form':form}
    return render(request, 'reviews/reviews.html',context)

# modal form: updating using a modal form
# an extra view created
def update(request,id):
    if request.method == 'POST':
        existing_data = Reviews.objects.get(pk=id)
        form = ReviewForm(request.POST,instance=existing_data)
        if form.is_valid():
            form.save()             # you can only save like this when you use the ModelForm
            return HttpResponseRedirect('thanks/')

    form = ReviewForm()
    context = {'form':form}
    return render(request, 'reviews/reviews.html',context)

def thank_you(request):
    return render(request,'reviews/thank_you.html')


# class based views

class ThankYouView(View):   #base view
    def get(self,request):
        return render(request,'reviews/thank_you.html')



# class ReviewView(View):      #base view
    def get(self,request):
        form = ReviewForm()
        context = {'form':form}
        return render(request,'reviews/reviews.html',context)
    
    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('thanks/')

# class ReviewView(FormView):                #Form view equivalent of ReviewView(View)
#     form_class = ReviewForm                  # This two lines handles the get and post functions 
#     template_name = 'reviews/reviews.html'
#     success_url = 'thanks2/'

#     def form_valid(self, form):  # This specific function's logic saves the form in the db
#         form.save()
#         return super().form_valid(form)

class ReviewView(CreateView):                 # Createview equivalent of the above based view
    model = Reviews                           # get the field needed to be used with the modal form
    form_class = ReviewForm                   # This three lines handles the get and post functions 
    template_name = 'reviews/reviews.html'
    success_url = 'thanks2/'                  # once successful saves the data to the model and redirects


class ThankYou(TemplateView):  # template view
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):                # passing  data to a template view
        context = super().get_context_data(**kwargs)     # this a dictionary already
        context['message'] = 'we are glad to be of help' # pass your contetnt to it as so
        return context                                   # return the output


# class ReviewsList(TemplateView):  # template view
#     template_name = 'reviews/reviews_list.html'

#     def get_context_data(self, **kwargs): 
#         context = super().get_context_data(**kwargs)
#         content = Reviews.objects.all()
#         context['contents'] = content
#         return context



# class SingleDetail(TemplateView):  # template view
#     template_name = 'reviews/single_review.html'

#     def get_context_data(self, **kwargs): 
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs['id']  # extract the id passed to the kwargs
#         reviews= Reviews.objects.get(pk=review_id)
#         context['reviews'] = reviews
#         return context


class ReviewsList(ListView):  # Listview
    template_name = 'reviews/reviews_list.html'
    model = Reviews
    context_object_name = 'contents'               # the name defined here is what you will use to querry 
                                                   # dynamic content in your templates 
                                                   # if not declared you will use 'object_list' to querry in ur templates

    # def get_queryset(self):                       # how to querry under listView
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gte=4)
    #     return data


class SingleDetail(DetailView):  # detail view
    template_name = 'reviews/single_review.html'
    model = Reviews  # the querry variable here is the name of the model in lower case, 'reviews' or 'object'
                     # this works more like a single view kinda thing
                     # note in the template used with this view, the querry variable is 'reviews'

    def get_context_data(self, **kwargs):                                           # This is all about accessing the stored session data and using it to make decisions here
        context = super().get_context_data(**kwargs)                                    # detail view context
        loaded_review = self.object                                              # how to get the objects stored in detailed view
        request = self.request                                                      # the request stored in detailed view
        # favorite_id = request.session['favorite_review']                           # getting a ppreviously stored session with a key, this will throw an error if no session is available
        favorite_id = request.session.get('favorite_review')                         # This handles the error incase no stored session is found
        context['is_favorite'] = favorite_id == str(loaded_review.id)             # comparing the previously stored session id n the object id, returns a boolean
        return context


class AddFavoriteView(View):
    def post(self,request):
        review_id = request.POST['review_id']
        # fav_review = Reviews.objects.get(pk=review_id) # don't store an object in as session
        request.session['favorite_review'] = review_id  # save the review id in session, this is a primitive data type
        return HttpResponseRedirect('/reviews/single_review/' + review_id) #go back to the same page

