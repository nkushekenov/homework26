from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ItemForm


def item_form(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('success'))
        else:
            return render(request, 'form.html', {'form': form})
    else:
        form = ItemForm()
        return render(request, 'form.html', {'form': form})

def success(request):
    return HttpResponse('Form submission successful!')
