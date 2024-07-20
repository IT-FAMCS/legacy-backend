from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Event
from .serializer import EventSerializer
from rest_framework.response import Response

class EventList(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Event.objects.prefetch_related('links').all()
    serializer_class = EventSerializer

class EventCreate(mixins.UpdateModelMixin, generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Event.objects.prefetch_related('links').all()
    serializer_class = EventSerializer

    def post(self, request, *args, **kwargs):
        short_title = request.data.get('short_title')
        if Event.objects.filter(short_title=short_title).exists():
            instance = Event.objects.get(short_title=short_title)
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return self.create(request, *args, **kwargs)
    
class EventUpdateView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Event.objects.prefetch_related('links').all()
    serializer_class = EventSerializer
    
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