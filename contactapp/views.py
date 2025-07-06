from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from .requestt import sendMsg


# Create your views here.
def sendMessage(request):
    contact_form = ContactForm()
    context = {'contact_form':contact_form}
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            msg = sendMsg(request.POST)
            messages.success(request, msg)
            contact_form = ContactForm()

    return render(request=request, template_name='contactapp/contact.html', context=context)