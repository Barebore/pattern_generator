from django.core.files.images import ImageFile
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
import base64
import os

from .logic.input_img_to_output_img import input_img_output_img
from .logic.list_to_input_img import list_to_input_img




class PatternAPIViewBase64(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        data = request.data
        username = data['username']
        pattern = data['pattern']
        try:
            directory, width, height = list_to_input_img(pattern, username)
        except Exception as e:
            return Response({'exception': str(e)}, status=406)
        input_img_output_img(width, height, directory)
        with open(directory, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        os.remove(directory)
        return Response({'pattern': encoded_string})


class TestPatternAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request):
        return Response({'test_get': 'get_successful'})

    def post(self, request):
        return Response({'test_post': 'post_successful'})
