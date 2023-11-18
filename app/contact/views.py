from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import AppealingForm
from .models import Contactinfo, Appealing

def contact(request):
    contact_info = Contactinfo.objects.first()
    form = AppealingForm()
    if request.method == "POST":
        form = AppealingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your appeal has been recorded and will be kept in touch soon.'))
            return redirect(reverse_lazy('contact'))
    
    context = {
        'contact_info': contact_info,
        "form": form,

    }
    return render(request, 'contact/index.html', context)
