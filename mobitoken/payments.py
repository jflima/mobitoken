from api.models import Client
from requests import get, post
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json

def get_super_seller():
    return Client.objects.get(zoop_id='1f82959f4a4a4516947be3e0f8930ef6')

def transfer(buyer, seller, amount):
    print(buyer.zoop_id)
    print(seller.zoop_id)
    try:
            
        r = post('https://api.zoop.ws/v2/marketplaces/%s/transfers/%s/to/%s'
                        % ('3249465a7753536b62545a6a684b0000', buyer.zoop_id,  seller.zoop_id),
                        params = {'amount': 10},
                        headers = {'Authorization': 'Basic enBrX3Rlc3RfRXpDa3pGRktpYkdRVTZIRnE3RVlWdXhJOg=='})
    except:
        pass
    buyer.balance -= amount
    seller.balance += amount

    buyer.save()
    seller.save()
    return r.text

# returns the balance
@api_view(['GET'])
@permission_classes((AllowAny, ))
def pay(self, token, seller_id, amount):
    buyer = None
    try:
        token = AliveTokens.objects.get(token=token)
        buyer = token.user
    except:
        return Response({"status": "500"})

    seller = Client.objects.filter(id=seller_id)

    if amount > buyer.get().balance:
        return Response({"status": "500"})

    response = transfer(buyer.get(), seller.get(), amount)
    text_response = json.loads(response)
    if "error" in text_response:
        return Response({"status": json.loads(response)["error"]["status_code"]})
    return Response({"status": "200"})

@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_cash(self, seller, amount = None):
    total_withdrawal = 0
    seller_obj = Client.objects.filter(zoop_id=seller)
    if amount is None:
        total_withdrawal = seller_obj.get().balance
    else:
        total_withdrawal = amount
    if total_withdrawal > seller_obj.get().balance:
        return Response({"status": "500"})

    response = transfer(seller_obj.get(), get_super_seller(), total_withdrawal)

    text_response = json.loads(response)
    if "error" in text_response:
        return Response({"status": json.loads(response)["error"]["status_code"]})
    return Response({"status": "200"})

@api_view(['GET'])
@permission_classes((AllowAny, ))
def send_boleto(self, token, amount):
    ## ROTINA DE ENVIO PARA EMAIL E VALIDACAO DO BOLETO
    ## MOCK COM A CONTA DE UM SUPERUSUARIO
    try:
        token = AliveTokens.objects.get(token=token)
        user = token.user
    except:
        return Response({"status": "500"})
    
    response = transfer(get_super_seller(), seller.zoop_id, amount)
    text_response = json.loads(response)
    if "error" in text_response:
        return Response({"status": json.loads(response)["error"]["status_code"]})
    return Response({"status": "200"})

