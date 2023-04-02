from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Name
from .forms import NameForm


def search_names(request):
    form = NameForm(request.GET or None)
    names = []
    if form.is_valid():
        search_text = form.cleaned_data['name']
        names = Name.objects.filter(name__icontains=search_text)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = [{'name': name.name} for name in names]
        return JsonResponse(data, safe=False)
    selected_names = request.GET.get('selected_names', '').split(',,')
    print(selected_names)
    return render(request, 'search_names.html', {'form': form, 'names': names})


def index(request):
    return render(request, 'index.html')


def ajax_view(request):
    name = request.POST.get('name')
    message = f'Hello, {name}!'
    # return a JSON response containing the data received from the Ajax request
    return JsonResponse({'message': message})
