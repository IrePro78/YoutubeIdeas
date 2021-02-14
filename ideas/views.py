from .models import Idea, Vote
from rest_framework import viewsets
from .serializer import IdeaSerialaizer, VoteSerializer

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerialaizer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
