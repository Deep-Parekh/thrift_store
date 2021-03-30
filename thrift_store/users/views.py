from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status

from users.models import CustomUser
from users.serializers import CustomUserSerializer

# GET list of user, POST a new user, DELETE all users
@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    # retrieve all users/find by username from MongoDB database
    if request.method == 'GET':
        users = CustomUser.objects.all()
        username = request.GET.get('username', None)

        if username is not None:
            users = users.filter(username__icontains=username)

        users_serializer = CustomUserSerializer(users, many=True)

        # safe = False for objects serialization
        return JsonResponse(users_serializer.data, safe=False)

    # create and save a new user
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = CustomUserSerializer(data=user_data)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete all users from the database
    elif request.method == 'DELETE':
        count = CustomUser.objects.all().delete()

        return JsonResponse({'message': '{} User were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# GET / PUT / DELETE user by ‘id’
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)

        # find a single user with an id
        if request.method == 'GET':
            user_serializer = CustomUserSerializer(user)
            return JsonResponse(user_serializer.data)

        # update a user by the id in the request
        elif request.method == 'PUT':
            user_data = JSONParser().parse(request)
            user_serializer = CustomUserSerializer(user, data=user_data)

            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data)

            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # delete a user with the specified id
        elif request.method == 'DELETE':
            user.delete()
            return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except CustomUser.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
