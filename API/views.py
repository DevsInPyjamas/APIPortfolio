import json

from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest
from API.decorators import cross_origin, returns_http_query
from API import models


@cross_origin
@returns_http_query
def all_projects(request):
    """
    The mighty power of all fucking projects serialized into a json
    :param request: the request
    :return: all the projects serialized into a json
    """
    max_elements = 10
    if request.method == 'GET' and 'count' in request.GET:
        max_elements = request.GET['count']
    query = models.Project.objects.filter()
    paginator = Paginator(query, max_elements)
    page
    return {"result": [p.to_dict() for p in models.Project.objects.all()]}


@cross_origin
@returns_http_query
def project(request):
    """
    The mighty power of one fucking project serialized into a json. The request should have an id
    if not, returns a bad request
    :param request: the request
    :return: the project serialized into a json
    """
    if request.method == 'GET' and 'id' in request.GET:
        id_project = request.GET['id']
        project_selected = models.Project.objects.filter(id=id_project).first()
        if project_selected is not None:
            return project_selected.to_dict()
    error_str = {'error': 'BAD REQUEST: There is no projects with that id.'}
    return HttpResponseBadRequest(json.dumps(error_str))


@cross_origin
@returns_http_query
def all_tags(request):
    """
    The mighty power of all fucking tags serialized into a json.
    :param request: the request
    :return: all tags serialized into a json
    """
    return {"result": [t.to_dict() for t in models.Tag.objects.all()]}


@cross_origin
@returns_http_query
def tag(request):
    """
    The mighty power of a fucking tag serialized into a json.
    :param request: the request
    :return: all tags serialized into a json
    """
    if request.method == 'GET' and 'id' in request.GET:
        id_tag = request.GET['id']
        tag_selected = models.Tag.objects.filter(id=id_tag).first()
        if tag_selected is not None:
            return tag_selected.to_dict()
    error_str = {'error': 'BAD REQUEST: There is no tags with that id.'}
    return HttpResponseBadRequest(json.dumps(error_str))
