from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models.practitioner import Practitioner
from api.serializers import PractitionerSerializer


@csrf_exempt
def practitioner_list(request):
    """
    List all practitioners, or create a new practitioner.
    """
    if request.method == "GET":
        practitioners = Practitioner.objects.all()
        serializer = PractitionerSerializer(practitioners, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PractitionerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def practitioner_detail(request, pk):
    """
    Retrieve, update or delete a code practitioner.
    """
    try:
        practitioner = Practitioner.objects.get(pk=pk)
    except Practitioner.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = PractitionerSerializer(practitioner)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PractitionerSerializer(practitioner, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        practitioner.delete()
        return HttpResponse(status=204)
