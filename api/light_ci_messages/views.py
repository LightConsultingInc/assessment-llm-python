from openai import OpenAI

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer
from django.conf import settings

# Make sure to set your OpenAI API key in your Django settings
client = OpenAI(
  api_key=settings.OPENAI_API_KEY
)

class MessageView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():

            messages = serializer.validated_data['messages']

            try:
                latestMessage = messages[-1]
                
                #### Call OpenAI API Here ####
                
                returnMessage = {
                    "role": "assistant",
                    "content": f"Message you sent: '{latestMessage['content']}'"
                }
                
                messages.append(returnMessage)

                return Response({
                    "messages": messages
                }, status=status.HTTP_200_OK)

            except Exception as e:

                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)