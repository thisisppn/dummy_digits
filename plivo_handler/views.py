from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
import json
from dummy_digits.settings import log, p
from plivo_handler.models import Messages


def index(request):
    response = p.get_numbers()
    log.debug(response)
    return JsonResponse(request.GET, safe=False)


@csrf_exempt
def receive_sms(request):
    if request.method == 'POST':
        log.debug(json.dumps(request.POST))
        message_type = request.POST.get('Type', None)
        if message_type != 'sms':
            log.error('Invalid message type: '+json.dumps(request.POST))
            return HttpResponseNotAllowed('Invalid message type')

        message_to = request.POST.get('To', None)
        message_from = request.POST.get('From', None)
        message = request.POST.get('Text', None)
        uuid = request.POST.get('MessageUUID', None)

        messageObj = Messages(
            uuid=uuid,
            message_to=message_to,
            message_from=message_from,
            message=message,
        )

        try:
            messageObj.save()
            return HttpResponse('OK')
        except Exception as e:
            log.error(type(e).__name__)
            log.error(str(e))
            return HttpResponseServerError('Not OK')
    else:
        return HttpResponseNotAllowed('Not OK')