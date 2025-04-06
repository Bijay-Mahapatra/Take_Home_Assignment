from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Incident
from .serializers import IncidentSerializer

class IncidentList(APIView):
    def get(self, request):
        incidents = Incident.objects.all()
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncidentDetail(APIView):
    def get_object(self, pk):
        try:
            return Incident.objects.get(pk=pk)
        except Incident.DoesNotExist:
            return None

    def get(self, request, pk):
        incident = self.get_object(pk)
        if incident is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = IncidentSerializer(incident)
        return Response(serializer.data)

    def delete(self, request, pk):
        incident = self.get_object(pk)
        if incident is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)