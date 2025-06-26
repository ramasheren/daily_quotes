from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

daily_quotes = {
    'sunday': 'be happy',
    'monday': 'be hopeful',
    'tuesday' : 'be positive',
    'wednesday' : 'be persistent',
    'thursday' : 'be bold',
    'friday' : 'be confident',
    'saturday' : 'be a winner'
}

days = list(daily_quotes.keys())

def index(request):
    day_list = ""
    for day in days:
        cap_day = day.capitalize()
        redirect_path = reverse('daily-quote', args = [day])
        day_list += f'<li><a href="{redirect_path}">{cap_day}</a></li>'
    data = f"<h1>Daily Quotes</h1><ul>{day_list}</ul>"
    return HttpResponse(data)

def daily_quote_by_num(request, day):
    redirect_day = days[day - 1]
    redirect_path = reverse('daily-quote', args = [redirect_day])  
    return HttpResponseRedirect(redirect_path)

def daily_quote(request, day):
    try:
        quote = daily_quotes[day]
        return HttpResponse(quote)
    except KeyError:
        return HttpResponseNotFound("not a day:(")
    
