
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer
from .models import ContactMessage
from .serializers import ContactMessageSerializer  # Import your serializer
from django.http import HttpResponse
from .sms_confirmation import sendsms


@api_view(['POST'])
def getbackend(request):
    if request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            mobile_number = serializer.validated_data.get('number')
            sendsms(mobile_number)

            return Response({'message': 'Data inserted successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def save_contact_message(request):
    if request.method == 'POST':
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            mobile_number = serializer.validated_data.get('telephone')
            sendsms(mobile_number)
            return Response({'message': 'Data inserted successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


from django.shortcuts import render

def index(request) : 
    return render(request, 'index.html')


from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    csrf_token = get_token(request)
    
    return JsonResponse({"csrfToken": csrf_token})
    
