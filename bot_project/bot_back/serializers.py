from rest_framework.serializers import ModelSerializer

from models import Questionary


class QuestionarySerializer(ModelSerializer):
    class Meta:
        model = Questionary
        fields = '__all__'
