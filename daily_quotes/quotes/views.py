from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

daily_quotes = {
    'sunday': 'be bold',
    'monday': 'be hopeful',
    'tuesday' : 'be positive',
    'wednesday' : 'be persistent',
    'thursday' : None,
    'friday' : 'be confident',
    'saturday' : 'be a winner'
}

days = list(daily_quotes.keys())

def index(request):

    return render(request, "quotes/index.html", {"days" : days})

def daily_quote_by_num(request, day):
    redirect_day = days[day - 1]
    redirect_path = reverse('daily-quote', args = [redirect_day])  
    return HttpResponseRedirect(redirect_path)

def daily_quote(request, day):
    try:
        quote = daily_quotes[day]
        return render(request, "quotes/quote.html", {
            "quote" : quote,
            "day" : day})
    except KeyError:
        data = render_to_string("quotes/404.html")
        return HttpResponseNotFound(data)
    
