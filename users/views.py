from rest_auth.views import LoginView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import render, redirect
from users.models import User
from users.serializers import UserSerializer
from api.models import Donor
from users.models import User



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
        if request.GET.get('gender', '') == "Male":
            search_gender = 1 
        elif (request.GET.get('gender', '')) == "Female":
            search_gender = 2
        else:
            search_gender = 0
        T = request.GET.get('bloodType', '')
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
        elif T == "AB-":
            search_blood_type = 8
        else:
            search_blood_type = 0
        if (search_id == "") & (search_gender == 0):
            donor = Donor.objects.filter(blood_type=search_blood_type).prefetch_related('id')
        elif (search_id == "") & (search_blood_type == 0):
            donor = Donor.objects.filter(gender = search_gender).prefetch_related('id')
        elif (search_blood_type != 0) & (search_gender != 0) & (search_id == ""):
            donor = ( Donor.objects.filter(blood_type=search_blood_type).prefetch_related('id') &
                     Donor.objects.filter(gender = search_gender).prefetch_related('id')
            )
        else:
            donor = Donor.objects.filter(id=search_id).prefetch_related('id')
        context = {
                'doners': donor
        }
        return render(request, "search.html", context)
    else:
        return redirect('/admin/')
