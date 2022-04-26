
from django.shortcuts import render
from datetime import date
import calendar
from calendar import HTMLCalendar
# Create your views here.

def index (request,year=date.today().year,month=date.today().month):
    year = int(year)
    month= int(month)
    if year <1900 or year >2099: year=date.today().year
    month_name = calendar.month_name[month]

    title= "Basic Calendar - %s %s" % (month_name,year)
    cal= HTMLCalendar().formatmonth (year,month)
    newsitems = [
     {
     'date': '27-01-2021', 'detail': "Semester 2 2019/2020 has started!"
     },
     {
     'date': '01-02-2021', 'detail': "Last Month of Winter!"
     }
     ]
    page_title="Second Django Lab"
    return render(request, 'base.html', {'title': title, 'cal': cal,
'newsitems': newsitems, 'page_title': page_title})

