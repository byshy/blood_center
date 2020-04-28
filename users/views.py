from rest_auth.views import LoginView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import render, redirect
from users.models import User
from users.serializers import UserSerializer
from api.models import Donor
from django.contrib import messages




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
        searchId = request.GET.get('ID', '')
        searchGender = 1 if (request.GET.get('gender', '')) == "male" else 2
        T = request.GET.get('bloodType', '')
        if (T == "A+"):
            searchBloodType = 1
        elif (T == "A-"):
            searchBloodType = 2
        elif (T == "B+"):
            searchBloodType = 3
        elif (T == "B-"):
            searchBloodType = 4
        elif (T == "O+"):
            searchBloodType = 5
        elif (T == "O-"):
            searchBloodType = 6
        elif (T == "AB+"):
            searchBloodType = 7
        else:
            searchBloodType = 8
        doner = (Donor.objects.filter(id = searchId) | Donor.objects.filter(gender = searchGender) | Donor.objects.filter(blood_type = searchBloodType))
        context = {
                'doners': doner
        }
        return render(request, "search.html", context)
    else:
        return redirect('/admin/')