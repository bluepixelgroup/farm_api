from rest_framework import serializers
from farm.models import Person, Fieldman, Farmer, PersonFamily


class PersonFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonFamily
        fields = ['id', 'relation_type', 'person']


class FielmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fieldman
        fields = '__all__'


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    relatives = PersonFamilySerializer(many=True, read_only=True)
    farmer = FarmerSerializer(many=False, read_only=True)
    fieldman = FielmanSerializer(many=False, read_only=True)

    class Meta:
        model = Person
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # remove null relations
        if not representation.get('farmer'):
            representation.pop('farmer')
        if not representation.get('fieldman'):
            representation.pop('fieldman')

        return representation
