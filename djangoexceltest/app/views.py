from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .resources import PersonResource
def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response