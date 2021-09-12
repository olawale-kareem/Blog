from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# static url views
# def jan(request):
#     return HttpResponse('Eat no meat for the entire month')
# def feb(request):
#     return HttpResponse('walk at least 20min everyday')

# dynamic url views

monthly_challenges ={
    "january": "Eat no meat for the entire month",
    "febuary": "workout everyday",
    "march": "got to the cinemas weekly",
    "april": "avoid sugar",
    "may": "go on a date",
    "june": "Eat no meat for the entire month",
    "july": "workout everyday",
    "august": "got to the cinemas weekly",
    "september": "avoid sugar",
    "octomber": "go on a date",
    "november": "Eat no meat for the entire month",
    "december": "workout everyday",

}

#  handles monthly: number format
def monthly_challenge_by_number(request, month):
    formatted_month = month - 1
    months = list(monthly_challenges.keys())
    if formatted_month >= 0 and month <= len(months):
        redirect_month = months[formatted_month]
        redirect_path = reverse('monthly-challenges', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound(f'Month number : {month} not supported!!')
       
# handles monthly: string format
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h1>{challenge_text}</h1>' 
        return HttpResponse(response_data)
    except:
        response_data = '<h1>Month not supported!!</h1>'
        return HttpResponseNotFound(response_data)

def challenge_list(request):
    months = list(monthly_challenges.keys())
    display_list = ''
    for month in months:
        capitalised_month = month.capitalize()
        month_link = reverse('monthly-challenges', args=[month])
        display_list += f"<li><a href='{month_link}'>{capitalised_month}</a></li>"
    response_data = f'<ul>{display_list}</ul>'
    return HttpResponse(response_data)


    
