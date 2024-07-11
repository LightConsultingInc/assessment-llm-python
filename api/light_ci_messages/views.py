import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer
from django.conf import settings

# Make sure to set your OpenAI API key in your Django settings
openai.api_key = settings.OPENAI_API_KEY

class MessageView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            messages = serializer.validated_data['messages']
            try:
                # Call OpenAI API
                response = openai.ChatCompletion.create(
                    model="gpt-4",  # or the appropriate model
                    messages=messages
                )
                return Response(response.choices[0].message, status=status.HTTP_200_OK)
            except openai.error.OpenAIError as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)