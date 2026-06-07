from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):

    @action(methods=['post'],detail=False,url_name='login')
    def login(self,request):
        print("Running good and setup done")
        return Response({'message':'Login Successful'},status=status.HTTP_200_OK)