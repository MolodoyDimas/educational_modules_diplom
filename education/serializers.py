from rest_framework import serializers

from education.models import Module
from education.validators import TitleValidator


class ModuleSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели образовательных модулей
    '''

    class Meta:
        model = Module
        fields = '__all__'
        validators = [TitleValidator(field='title')]
        serializers.UniqueTogetherValidator(fields=['title'],
                                            queryset=Module.objects.all())
