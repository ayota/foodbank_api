from django.http import HttpResponse
from restapi.models import Scan, FoodCat, WellScore, NutRule, UPC
from rest_framework import viewsets
from django.views.generic import ListView, View
from restapi.serializers import UPCSerializer, ScanSerializer, FoodCatSerializer, WellScoreSerializer, NutRuleSerializer
from restapi.process_upc import Food
import os
from json import dumps
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class ScanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Scan.objects.all().order_by('-created')
    serializer_class = ScanSerializer


class FoodCatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FoodCat.objects.all().order_by('-created')
    serializer_class = FoodCatSerializer


class WellScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = WellScore.objects.all().order_by('-created')
    serializer_class = WellScoreSerializer


class NutRuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = NutRule.objects.all().order_by('-created')
    serializer_class = NutRuleSerializer


class UPCViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UPC.objects.all().order_by('-created')
    serializer_class = UPCSerializer

def scan_view(request,upc):
	'''
	This will be what the app sends.
	The url format is URL_STUFF/{some upc code}/?food_cat={some food cat}
	It will return JSON with the item name, wellness score, and API status.
	'''
	food_cat = request.GET.get('food_cat')
	api_key = os.environ.get('api_key', '')  # api_key
	api_id = os.environ.get('api_id', '') # api_id
	item = Food(str(upc), food_cat, api_key, api_id)

	try:
		upc_pk = UPC.objects.values_list('pk',flat=True).get(upc_code=upc)
	except ObjectDoesNotExist:
		upc_pk = None 

	try:
		food_cat_pk = FoodCat.objects.values_list('pk', flat=True).get(load_cat=food_cat)
	except ObjectDoesNotExist:
		food_cat_pk = None
	
	# do scanner update
	obj = Scan(upc_id_id=upc_pk, upc_raw=upc, food_cat_id_id=food_cat_pk, scan_status=item.api_response.values()[0])
	obj.save()

	# format response for the app
	app_data = { 
	'product': item.food_info,
	'wellness' : item.wellness,
	'response' : item.api_response.keys()[0],
	'message' : item.api_response.values()[0]
	}

	return HttpResponse(dumps(app_data, indent=4, sort_keys=True, default=lambda x:str(x)), content_type="application/json")








