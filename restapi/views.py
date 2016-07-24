from restapi.models import Scan, FoodCat, WellScore, NutRule, UPC
from rest_framework import viewsets
from restapi.serializers import UPCSerializer, ScanSerializer, FoodCatSerializer, WellScoreSerializer, NutRuleSerializer


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
