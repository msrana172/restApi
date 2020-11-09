from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import * 
class UserList(APIView):
    def get(self, request): 
        model = Users.objects.all()
        serializer = UsersSerializer(model, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = UsersSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class UserDetail(APIView):
    def get_user(self, employee_id):
        try:
            model = Users.objects.get(id = employee_id)
            return model
        except Users.DoesNotExist:
            return 
            # Response(f'User with {employee_id} is not found in database', status=status.HTTP_404_NOT_FOUND)    

    def get(self, request, employee_id): 
        # try:
        #     model = Users.objects.get(id = employee_id)
        # except Users.DoesNotExist:
        #     return Response(f'User with {employee_id} is not found in database', status=status.HTTP_404_NOT_FOUND)    
        # serializer = UsersSerializer(model)
        if not self.get_user(employee_id):
            return Response(f'User with {employee_id} is not found in database', status=status.HTTP_404_NOT_FOUND)
            
        serializer = UsersSerializer(self.get_user(employee_id))
        return Response(serializer.data)
    def put(self, request, employee_id):
        # try:
        #     model = Users.objects.get(id = employee_id)
        # except Users.DoesNotExist:
        #     return Response(f'User with {employee_id} is not found in database', status=status.HTTP_404_NOT_FOUND) 
        # serializer = UsersSerializer(model, data = request.data)
        serializer = UsersSerializer(self.get_user(employee_id), data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, employee_id):
        model = self.get_user(employee_id)
        model.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

