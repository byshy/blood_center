from django.http import Http404

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import BloodCenter
from api.permissions import ReadOnly
from api.serializers import BloodCenterSerializer


class BloodCenterListView(generics.ListAPIView):
    http_method_names = ['get']
    serializer_class = BloodCenterSerializer
    queryset = BloodCenter.objects.all()
    permission_classes = [ReadOnly]


class BloodCenterView(APIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return BloodCenter.objects.get(name=id)
        except BloodCenter.DoesNotExist:
            raise Http404

    def get(self, request, id):
        try:
            pp = self.get_object(id)
            serializer = BloodCenterSerializer(pp)
            content = {
                'data': serializer.data,
                'msg': 'element retrieved successfully',
                'status': status.HTTP_200_OK
            }
            return Response(content)
        except Http404:
            return Response({'msg': 'element not found', 'status': status.HTTP_404_NOT_FOUND})