from rest_framework import serializers
from .models import Event, Links

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['id', 'link', 'title']

class EventSerializer(serializers.ModelSerializer):
    links = LinksSerializer(many=True)

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        links_data = validated_data.pop('links', [])
        event_name = validated_data.get('short_title')

        try:
            event = Event.objects.get(short_title=event_name)
            for key, value in validated_data.items():
                setattr(event, key, value)
            event.save()

            for link_data in links_data:
                Links.objects.update_or_create(event=event, **link_data)
        except Event.DoesNotExist:
            event = Event.objects.create(**validated_data)
            for link_data in links_data:
                Links.objects.create(event=event, **link_data)
                
        return event

    def update(self, instance, validated_data):
        links_data = validated_data.pop('links', [])
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        # Updating links
        for link_data in links_data:
            link_id = link_data.get('id')
            if link_id:
                link = Links.objects.get(id=link_id, event=instance)
                for key, value in link_data.items():
                    setattr(link, key, value)
                link.save()
            else:
                Links.objects.create(event=instance, **link_data)

        return instance
