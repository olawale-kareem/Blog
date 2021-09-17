from django import forms
from .models import Reviews

# manual form
# class ReviewForm(forms.Form):
#     err_context = {'required':'Your name must not be empty', 'max_length':'Please enter a short name'}
#     user_name = forms.CharField(label='userName', max_length=100, error_messages=err_context)
#     review_text = forms.CharField(label='reviews')
#     rating = forms.IntegerField()

# Model form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        # fields = ['user_name', 'review_text', 'rating']
        fields = '__all__'   # to select all fields of the form
        # exclude = ['']    # This is to exclude some certain field
        labels = {
        'user_name': 'UserName',
        'review_text': 'Your Feedback',
        'rating':'Your Rating'
        }

        error_messages = { 
           ' user_name' :{
                'required': 'Your name must not be empty',
                'max_length': 'Please enter a short name'
            }     
        }

        






