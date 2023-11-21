from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import QuestionarySerializer
from .models import Questionary
from rest_framework.response import Response


# Create your views here.
class QuestionaryList(APIView):
    def get(self, *args, **kwargs):
        queryset = Questionary.objects.all()
        serialized_question = QuestionarySerializer(queryset, many=True)
        return Response(serialized_question.data)
