from rest_framework import serializers

from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = [
            'name',
            'species',
            'age'
        ]


class ListAnimalSerializer(serializers.ModelSerializer):

    data = serializers.SerializerMethodField()

    def get_data(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            if obj.owner == user:
                return {"name": obj.name,
                        "age": obj.age}
        return "Age and name unknown"

    class Meta:
        model = Animal
        fields = [
            'species',
            'data'
        ]
