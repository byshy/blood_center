from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.serializers import UserSerializer


class CreateUserViewSet(generics.CreateAPIView):
    # create a new user account
    http_method_names = 'post'
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {
                'data': {
                    'pk': serializer.data.get('pk'),
                    'email': serializer.data.get('email'),
                    'first_name': serializer.data.get('first_name'),
                    'last_name': serializer.data.get('last_name'),
                    'mobile': serializer.data.get('mobile'),
                },
                'msg': 'account created successfully',
                'status': status.HTTP_201_CREATED
            }
            return Response(content)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
