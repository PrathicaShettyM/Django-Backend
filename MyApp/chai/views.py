from django.shortcuts import render
from django.http import HttpResponse
from .models import ChaiVariety
from django.shortcuts import get_object_or_404


# Create your views here.
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais':chais})
    # request, template file, send all chais object

# show a seperate description field
def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai':chai})





















def order(request):
    return HttpResponse("Order your chai here")
