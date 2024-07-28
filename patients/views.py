from django.shortcuts import render
from patients.models import Patients


def listPatients(request):

    context = {
        "title": "MedIBox - Пациенты",
        "content": "пампампам"
    }

    return render(request, 'allPatients.html', context)


def patient(request): #client_slug

    # client = Clients.objects.get(slug=client_slug)
    client = 0

    context = {
        'title': 'MedIBox - пациент',
        'client': client,
        'content': 'всякая всячина'
    }
    return render(request, 'patient.html', context)