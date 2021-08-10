from django.shortcuts import render,get_object_or_404
from .models import *

from django.views.generic import (
	TemplateView,
	ListView,
	DetailView
	)

import telepot

TOKEN = '1717842899:AAGP5Vs5F44ueMdf-VXVEAfOBbmdaMfspW8'
my_id = '524971654'
# Create your views here.

def get_all_categories(request):
	
    context = {
        'categories':TransportCategory.objects.all()
    }
    return context


def homePage(request):

	city = City.objects.all().order_by('?')[:4]
	cars = Transport.objects.all().order_by('?')[:3]

	context = {
		'cities':city,
		'cars':cars,
	}

	return render(request,'index.html',context)


def grafik(request):

	fort = FortGrafik.objects.all()
	bus = BusGrafik.objects.all()

	context = {
		'forts':fort,
		'busses':bus
	}
	return render(request,'grafik.html',context)

class TransportPageView(ListView):
	model = Transport
	paginate_by = 6
	template_name = 'transports.html'


def categoryDetailPage(request, category_slug):
    category = get_object_or_404(TransportCategory, slug=category_slug)
    print(category)
    transport = Transport.objects.filter(category=category)

    context = {
        'cars_category':transport,
    }

    return  render(request, 'category-detail.html',context)



def contactPage(request):

	if request.method == 'POST':
		n = request.POST['name']
		t = request.POST['number']
		e = request.POST['email']
		m = request.POST['message']
		bot = telepot.Bot(TOKEN)
		bot.sendMessage(my_id, f'Ismi: {n}\nNomeri: {t}\nEmaili: {e}\nXabari: {m}')
		Contact.objects.create(name=n,number=t,email=e,message=m)

	return render(request,'contact.html')

class TransportDetailView(DetailView):
	model = Transport