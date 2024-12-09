from django.shortcuts import render
from django.http import HttpResponse
from .models import ChaiVariety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais':chais})
    # request, template file, send all chais object

# show a seperate description field
def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai':chai})

# write function
def chai_store_view(request):
    stores = None
    # form submit
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chai_variety)
    
    else:
        # give option for user to fill form
        form = ChaiVarietyForm()  
    
    return render(request, 'chai/chai_stores.html', {'stores':stores, 'form':form})
# write url for this



















def order(request):
    return HttpResponse("Order your chai here")
