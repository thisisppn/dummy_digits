from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from dummy_digits.settings import log

def index(request):
    print(request.GET)
    return JsonResponse(request.GET, safe=False)

@csrf_exempt
def receive_sms(request):

    log.debug(json.dumps(request.POST))

    sms_to = request.POST.get('To', None)
    sms_from = request.POST.get('From', None)
    message = request.POST.get('Text', None)
    sms_id = request.POST.get('MessageUUID', None)
    # response = p.get_numbers()
    # print(response)

    return JsonResponse('OK', safe=False)