from rest_framework.decorators import api_view
from django.shortcuts import redirect

@api_view(['GET'])
def redirect_view(request):
    response = redirect('admin/')
    return response