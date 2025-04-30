
def get_required_param(request, param_name):
    value = request.GET.get(param_name)
    if not value:
        raise ValueError(f"Missing '{param_name}' parameter")
    return value

