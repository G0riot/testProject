from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import QuestionarySerializer
from .models import Questionary
from rest_framework.response import Response


# Create your views here.
class QuestionaryList(APIView):
    def get(self, *args, **kwargs):
        queryset = Questionary.objects.all()
        serializer = QuestionarySerializer(queryset, many=True)
        return Response(serializer.data)

    '''def get_retrieve(self, request, pk=None):
        queryset = Questionary.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = QuestionarySerializer(user)
        return Response(serializer.data)'''
