from API import cross_origin, returns_json


@cross_origin
@returns_json
def all_projects(request):
    """
    The mighty power of
    :param request:
    :return:
    """
    query_response = ''
    dicted_response = ''
    return dicted_response