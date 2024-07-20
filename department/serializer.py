from rest_framework import serializers
from .models import Department, Links

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['id', 'link', 'title']

class DepartmentSerializer(serializers.ModelSerializer):
    links = LinksSerializer(many=True)

    class Meta:
        model = Department
        fields = '__all__'

    def create(self, validated_data):
        links_data = validated_data.pop('links', [])
        depart_name = validated_data.get('short_title')

        try:
            department = Department.objects.get(short_title=depart_name)
            for key, value in validated_data.items():
                setattr(department, key, value)
            department.save()

            for link_data in links_data:
                Links.objects.update_or_create(department=department, **link_data)
        except Department.DoesNotExist:
            department = Department.objects.create(**validated_data)
            for link_data in links_data:
                Links.objects.create(department=department, **link_data)
                
        return department

    def update(self, instance, validated_data):
        links_data = validated_data.pop('links', [])
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        # Updating links
        for link_data in links_data:
            link_id = link_data.get('id')
            if link_id:
                link = Links.objects.get(id=link_id, department=instance)
                for key, value in link_data.items():
                    setattr(link, key, value)
                link.save()
            else:
                Links.objects.create(department=instance, **link_data)

        return instance
