from django import template

register = template.Library()


@register.filter(name="hx-querybuilder")
def hx_querybuilder(request_dict, **kwargs):
    """
    This filter is used to build a query string for htmx requests.
    :param request_dict: The request.GET dictionary
    :param kwargs: The query parameters to add to the request
    :return: A query string
    """
    query = request_dict.copy()
    query.update(kwargs)
    return query.urlencode()


@register.filter(name="hx-querysubtract")
def hx_querysubtract(request_dict, **kwargs):
    """
    This filter is used to remove query parameters from a query string for htmx requests.
    :param request_dict: The request.GET dictionary
    :param kwargs: The query parameters to remove from the request
    :return: A query string
    """
    query = request_dict.copy()
    for key in kwargs:
        if key in query:
            del query[key]
    return query.urlencode()
