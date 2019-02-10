
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes((AllowAny, ))
def obterToken(self):
    print "MEU TOKEN EH "
    return Response({"message": "TOKEN"})

@api_view(['GET'])
@permission_classes((AllowAny, ))
def validarToken(self, latitude, longitude):
    print "MEU TOKEN EH "
    return Response({"message": "VALID TOKEN", "latitude": latitude, "longitude": longitude})
