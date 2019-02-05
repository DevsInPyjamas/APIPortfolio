import json

from django.http import HttpResponseBadRequest

from API.decorators import cross_origin, returns_json
from API import models
from django.core import serializers


@cross_origin
@returns_json
def all_projects(request):
    """
    The mighty power of all fucking projects serialized into a json
    :param request: the request
    :return: all the projects serialized into a json
    """
    return serializers.serialize('json', models.Project.objects.all())


@cross_origin
@returns_json
def project(request):
    """
    The mighty power of one fucking project serialized into a json. The request should have an id
    if not, returns a bad request
    :param request: the request
    :return: the project serialized into a json
    """
    if request.method == 'GET' and 'id' in request.GET:
        id_project = request.GET['id']
        return serializers.serialize('json', models.Project.objects.filter(id_project))
    error_str = {'error': 'BAD REQUEST: There is no projects with that id.'}
    return HttpResponseBadRequest(json.dumps(error_str))
