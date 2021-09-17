from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View


from .forms import ReviewForm
from .models import Reviews


def reviews(request):
    # modal form
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save() # you can only save like this when you use the ModelForm
            return HttpResponseRedirect('thanks/')

    form = ReviewForm()
    context = {'form':form}
    return render(request, 'reviews/reviews.html',context)


    # manual form: saving to the database using a manual form
    # if request.method == 'POST':
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         review = Reviews.objects.create(user_name=form.cleaned_data['user_name'],
    #                                         review_text=form.cleaned_data['review_text'],
    #                                         rating=form.cleaned_data['rating']
    #                                         )
    #         review.save()
    #         return HttpResponseRedirect('thanks/')

    # form = ReviewForm()
    # context = {'form':form}
    # return render(request, 'reviews/reviews.html',context)

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

# class based view

class ReviewView(View):
    def get(self,request):
        form = ReviewForm()
        context = {'form':form}
        return render(request,'reviews/reviews.html',context)
    
    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('thanks/')

