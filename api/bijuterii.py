from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from bijuterii.models import Bijuterie, Culoareaur, BijuterieCuloareaur


class BijuteriePaginator(PageNumberPagination):
    page_size = 4
    max_page_size = 4


class CuloareaurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culoareaur
        exclude = []


class BijuterieCuloareaurSerializer(serializers.ModelSerializer):
    culoareaur = CuloareaurSerializer()

    class Meta:
        model = BijuterieCuloareaur
        exclude = []

class BijuterieSerializer(serializers.ModelSerializer):

    culoriaur = BijuterieCuloareaurSerializer(many=True, source='category_pivot')

    class Meta:
        model = Bijuterie
        exclude = []

class BijuterieViewSet(viewsets.ModelViewSet):
    serializer_class = BijuterieSerializer
    queryset = Bijuterie.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = BijuteriePaginator

# class BijuterieCuloareaur(serializers.ModelSerializer):
#     culoareaur = CuloareaurSerializer()
#
#     class Meta:
#         model = BijuterieCuloareaur
#         exclude = []