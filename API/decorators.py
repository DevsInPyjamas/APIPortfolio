import json

from django.http import HttpResponse


def cross_origin(func):
    def cross_origin_decorator(request):
        response = func(request)
        if isinstance(response, HttpResponse):
            response['Access-Control-Allow-Origin'] = '*'
            if request.method == 'OPTIONS':
                response['Access-Control-Allow-Headers'] = 'x-session-user'
                response['Access-Control-Allow-Methods'] = 'GET, POST, DELETE'
        return response

    return cross_origin_decorator


def returns_http_query(func):
    """
    Just a decorator pattern application to a method. It checks if it is returning a HETTPReponse, if it not, then
    creates a HTTPResponse and returns it. Also adds the format of the response.
    :param func: a function to enlarge its behaviour
    :return: HTTPResponse of a request.
    """
    def returns_json_decorator(request):
        response = func(request)
        if isinstance(response, HttpResponse):
            response['Content-Type'] = 'application/json; charset=utf-8'
        else:
            response = HttpResponse(json.dumps(response))
            # response = HttpResponse(response)
            response['Content-Type'] = 'application/json; charset=utf-8'
        return response

    return returns_json_decorator
