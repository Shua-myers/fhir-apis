from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from api.models.practitioner import Practitioner
from api.serializers import PractitionerSerializer


@api_view(["GET", "POST"])
def practitioner_list(request: Request) -> Response:
    """
    List all practitioners, or create a new practitioner.
    """
    if request.method == "GET":
        practitioners = Practitioner.objects.all()
        serializer = PractitionerSerializer(practitioners, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        # TODO: get this actually working - create works but none of the related models are being written to correctly
        serializer = PractitionerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def practitioner_detail(request: Request, pk: int) -> Response:
    """
    Retrieve, update or delete a code practitioner.
    """
    try:
        practitioner = Practitioner.objects.get(pk=pk)
    except Practitioner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PractitionerSerializer(practitioner)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PractitionerSerializer(practitioner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        practitioner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
