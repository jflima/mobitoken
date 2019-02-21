
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import random
from api.models import AliveToken, Client
from datetime import datetime, timedelta

@api_view(['GET'])
@permission_classes((AllowAny, ))
def obterToken(self, latitude, longitude):
	params_local = {"latitude": latitude, "longitude": longitude}
	t = None
	while not t:
		generated_token = ""
		for x in range(6):
			generated_token += str(random.randint(0,9))
		alive_tokens = AliveToken.objects.raw("SELECT * FROM api_alivetoken WHERE api_alivetoken.token = %s", [generated_token])
		if len(list(alive_tokens)) == 0:
			now = datetime.now()
			end = now + timedelta(seconds = 31)
			t = AliveToken.objects.create(token=generated_token, user=Client.objects.filter(pk=1)[0], local=params_local, beginning_at=now, end_at=end)
			t.refresh_from_db()
	return Response({"token": t.token})

@api_view(['GET'])
@permission_classes((AllowAny, ))
def validarToken(self, latitude, longitude):
    print("MEU TOKEN EH ")
    return Response({"message": "VALID TOKEN", "latitude": latitude, "longitude": longitude})
