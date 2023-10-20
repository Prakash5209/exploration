from django.shortcuts import render,redirect

from dynamic_formset.forms import ContactForm
from dynamic_formset.models import Contact

def index(request):
    context = {'form':ContactForm(),'contacts':Contact.objects.all()}
    return render(request,'home.html',context)

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact = form.save()
            context = {'contact':contact}
            return render(request,'contact.html',context)
    return render(request,'form.html',{'form':ContactForm})