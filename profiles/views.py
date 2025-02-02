from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProfileSerializer

from .models import Profile

class ProfileListView(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

