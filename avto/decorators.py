from django.shortcuts import get_object_or_404, redirect

from .models import Auto


def is_owner(views):

    def inner_func(request, id, *args, **kwargs):
        Auto = get_object_or_404(Auto, id=id)

        if Auto.author == request.user:
            return views(request, id, *args, **kwargs)
        
        return redirect('/auto/')

    return inner_func
