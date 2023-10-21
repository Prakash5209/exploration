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
    if request.method == 'POST':
        form = DemoModelForm(request.POST or None)
        if form.is_valid():
            demomodels.name = form.cleaned_data['name']
            demomodels.title = form.cleaned_data['title']
            # print(f"------------{name}-----------{title}")
            # demomodels(name = name, title = title).save()
            demomodels.save()
            return redirect('demo:demohome')
    context = {'demomodels':demomodels}
    return render(request,'update.html',context)
