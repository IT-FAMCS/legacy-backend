from rest_framework import serializers
from .models import Information

class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Information
        fields = '__all__'

    def create(self, validated_data):
        info_name = validated_data.get('short_title')

        try:
            info = Information.objects.get(short_title=info_name)
            for key, value in validated_data.items():
                setattr(info, key, value)
            info.save()

        except Information.DoesNotExist:
            info = Information.objects.create(**validated_data)
                
        return info

    def update(self, instance, validated_data):
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()


        return instance
