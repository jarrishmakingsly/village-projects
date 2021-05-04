from django.shortcuts import render
from .forms import PanchayathForm
from .models import Panchayath
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages



def index(request):
    return render(request, "index.html")

# Create your views here.
def register_panchayath(request):
    register_url = reverse('villageapp:register_panchayath')
    if request.method == 'POST':
        register_form = PanchayathForm(data=request.POST)
        if register_form.is_valid():
            item = register_form.save()
            item.save()
            messages.success(request, 'Successfully created a Panchayath entity')
            return redirect('villageapp:index')
        else:
            return render(request,
            'register.html',
            {'register_form': register_form, 'register_url': register_url} )
    else:
        register_form = PanchayathForm()
        return render(request,
            'register.html',
            {'register_form': register_form, 'register_url': register_url} )
