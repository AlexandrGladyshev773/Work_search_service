from django.shortcuts import render
from datetime import datetime

def home(request):
    date = datetime.now().date()
    name = 'Alex'
    _context = {'date':date, 'name':name}
    return render(request, 'home.html', _context)