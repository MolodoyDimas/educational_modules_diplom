from rest_framework import generics
from rest_framework.permissions import AllowAny
from education.models import Module
# from education.paginators import ModulePaginator
# from education.permissions import IsMember, IsModerator
from education.serializers import ModuleSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    serializer_class = ModuleSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsModerator]


class ModuleListAPIView(generics.ListAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsMember, IsModerator]
    # pagination_class = ModulePaginator


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsModerator]


class ModuleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsModerator]


class ModuleDestroyAPIView(generics.DestroyAPIView):
    queryset = Module.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsModerator]
