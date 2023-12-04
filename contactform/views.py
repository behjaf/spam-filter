import re

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from contactform.models import ContactUs


# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'contactus.html')

    else:
        consecutive_repeats = any(request.POST['bodytext'][i] == request.POST['bodytext'][i + 1] for i in range(len(request.POST['bodytext']) - 1))
        if consecutive_repeats:
            return HttpResponse("you typed so many text with the same letter")

        if ContactUs.objects.filter(email=request.POST['emailaddress']):
            return HttpResponse("you contacted us. wait for response")

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, request.POST['emailaddress']):
            ContactUs.objects.create(name=request.POST['firstname'], email=request.POST['emailaddress'],
                                     body=request.POST['bodytext'])
            return HttpResponse("Data saved successfully.")
        return HttpResponse("invalid email")
