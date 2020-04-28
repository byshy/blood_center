from rest_auth.views import LoginView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import render, redirect
from users.models import User
from users.serializers import UserSerializer
from api.models import Donor


class CreateUserViewSet(generics.CreateAPIView):
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


class CustomLoginView(LoginView):

    def get_response(self):
        original_response = super().get_response()
        user = User.objects.filter(pk=original_response.data['user']['pk'])
        user_data = UserSerializer(user, many=True)
        print(user_data.data)
        response = {
            'token': original_response.data['token'],
            'user': user_data.data
        }
        return Response(data=response)


def searchView(request):
    if request.user.is_authenticated:
        search_id = request.GET.get('ID', '')
        # search_gender = request.GET.get('gender', '')
        search_gender = 1 if (request.GET.get('gender', '')) == "male" else 2
        T = request.GET.get('bloodType', '')
        # search_blood_type = request.GET.get('bloodType', '')
        if T == "A+":
            search_blood_type = 1
        elif T == "A-":
            search_blood_type = 2
        elif T == "B+":
            search_blood_type = 3
        elif T == "B-":
            search_blood_type = 4
        elif T == "O+":
            search_blood_type = 5
        elif T == "O-":
            search_blood_type = 6
        elif T == "AB+":
            search_blood_type = 7
        else:
            search_blood_type = 8

        donor = (
                Donor.objects.filter(id=search_id) |
                Donor.objects.filter(gender=search_gender) |
                Donor.objects.filter(blood_type=search_blood_type)
                )

        context = {
                'doners': donor
        }
        return render(request, "search.html", context)
    else:
        return redirect('/admin/')
