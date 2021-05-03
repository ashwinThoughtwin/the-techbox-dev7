from rest_framework import serializers
from .models import TechBox, IssueGadget

class TechBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechBox
        fields = '__all__'


class IssueGadgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueGadget
        fields = '__all__'