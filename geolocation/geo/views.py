from django.shortcuts import render

from .forms import GeoForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = GeoForm(request.POST)
        if form.is_valid():
            initial = form.cleaned_data['initial']
            destination = form.cleaned_data['destination']
            # Here you would typically process the data, e.g., save it or perform some action
            return render(request, 'geo/result.html', {'initial': initial, 'destination': destination})
    else:
        form = GeoForm()

    return render(request, 'geo/index.html', {'form': form})