# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render



# from rest_framework import generics
from api.models import Client
# from api.serializers import ClientSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ClientList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        return Client.objects.all()
