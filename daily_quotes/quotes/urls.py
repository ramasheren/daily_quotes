from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:day>/", views.daily_quote_by_num),
    path("<str:day>/", views.daily_quote, name="daily-quote"),
]