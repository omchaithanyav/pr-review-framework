from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from pprint import pprint


@api_view(['POST'])
@permission_classes([AllowAny])
def github_webhook(request):
    data = request.data
    if data:
        pprint(f'Webhook received: {data}')
    return Response({'message': 'Webhook processed'}, status=status.HTTP_200_OK)
