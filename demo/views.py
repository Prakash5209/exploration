from django.shortcuts import render,redirect

from demo.forms import DemoModelForm
from demo.models import DemoModel

def demohome(request):
    demomodels = DemoModel.objects.all()
    if request.method == 'POST':
        form = DemoModelForm(request.POST or None)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # title = form.cleaned_data['title']
            name = request.POST.get('name')
            title = request.POST.get('title')
            DemoModel(name = name, title = title).save()
            return redirect('demo:demohome')
    else:
        form = DemoModelForm()
    context = {'form':form,'demomodels':demomodels}
    return render(request,'demo.html',context)


def updatedemo(request,id):
    demomodels = DemoModel.objects.get(id = id)
    form = DemoModelForm(request.POST or None)
    # if form.is_valid():
    #     name = form.cleaned_data['name']
    #     title = form.cleaned_data['title']
    #     DemoModel(name = name, title = title).save()
    # else:
    #     form = DemoModelForm()
    context = {'demomodels':demomodels,'form':form}
    return render(request,'update.html',context)
