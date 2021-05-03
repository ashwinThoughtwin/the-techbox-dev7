from .models import TechBox, IssueGadget
from .serializers import TechBoxSerializer, IssueGadgetSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
class TechBoxAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None, format=None):
        if pk is None:
            data = TechBox.objects.all()
            serializer = TechBoxSerializer(data, many=True)
            return Response(serializer.data)
        else:
            data = TechBox.objects.get(id=pk)
            serializer = TechBoxSerializer(data)
            return Response(serializer.data)


    def post(self, request, format=None):
        serializer = TechBoxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        item = TechBox.objects.get(id=pk)
        serializer = TechBoxSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg': 'Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = TechBox.objects.get(id=pk)
        data.delete()
        return Response({'Msg': 'Data Deleted'})


# class IssueGadgetAPI(ListCreateAPIView):
#     queryset = IssueGadget.objects.all()
#     serializer_class = IssueGadgetSerializer

class IssueGadgetAPI(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        data = IssueGadget.objects.all()
        serializer = IssueGadgetSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IssueGadgetSerializer(data=request.data)
        if serializer.is_valid():
            # print(request.data)
            # print(request.data['gadget_name'])
            gadget_id = request.data['gadget_name']
            gadget_data = TechBox.objects.get(id=gadget_id)
            print(gadget_data)
            available = gadget_data.available
            if available:
                serializer.save()
                return Response({'Msg': f'{gadget_data.name} is issued to you.'})
            else:
                return Response({'Msg': f'{gadget_data.name} is not available.'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


