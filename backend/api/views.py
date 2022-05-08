from pyexpat import model
from django.shortcuts import render
# from django.http import JsonResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    data = {}
    model_data = Product.objects.all().order_by('?').first()

    if model_data:
        data = model_to_dict(model_data)
    return Response(data)
