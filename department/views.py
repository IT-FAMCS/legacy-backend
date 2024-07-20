from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Department
from .serializer import DepartmentSerializer
from rest_framework.response import Response

class DepartmentList(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Department.objects.prefetch_related('links').all()
    serializer_class = DepartmentSerializer
    
   


class DepartmentCreate(mixins.UpdateModelMixin, generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Department.objects.prefetch_related('links').all()
    serializer_class = DepartmentSerializer

    def post(self, request, *args, **kwargs):
        short_title = request.data.get('short_title')
        if Department.objects.filter(short_title=short_title).exists():
            instance = Department.objects.get(short_title=short_title)
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return self.create(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

    
class DepartmentUpdateView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Department.objects.prefetch_related('links').all()
    serializer_class = DepartmentSerializer
    
    lookup_field = "short_title"
    


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)