from rest_framework.viewsets import ModelViewSet
from .serializers import QuestionarySerializer
from .models import Questionary


# Create your views here.
class QuestionaryViewSet(ModelViewSet):
    queryset = Questionary.objects.all()
    serializer_class = QuestionarySerializer

