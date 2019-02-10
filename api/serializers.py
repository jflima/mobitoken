# from models import Client
# from rest_framework import routers, serializers, viewsets
# from rest_framework import mixins
# from rest_framework import generics

# # Serializers define the API representation.
# class ClientSerializer():
#     class Meta:
#         model = Client
#         fields = ('id', 'name', 'email', 'phone')
    
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True)
#     email = serializers.CharField(required=True)
#     phone = serializers.CharField(required=True)


#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)