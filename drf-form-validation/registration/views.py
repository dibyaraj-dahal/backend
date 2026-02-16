from rest_framework import status
from rest_framework.views import APIView
from .models import Registration
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import RegistrationSerializer
from rest_framework.response import Response
# Create your views here.


class RegistrationListAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Registration successful!',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
