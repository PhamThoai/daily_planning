from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsOwnerPermission
from django.contrib.auth.models import User
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import (
    PersonalSettingSerializer,
    EventSerializer,
    PlanForDaySerializer,
    EvaluationForDaySerializer,
    EvaluationSerializer,
    LongTermPlanSerializer,
    ShortTermPlanSerializer
)
from myplan.models import (
    PersonalSetting,
)

class PersonalSettingDetail(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    serializer_class = PersonalSettingSerializer

    def get_object(self):
        try:
            user = request.user
        except User.DoesNotExist:
            raise Http404

        try:
            personal_setting = user.personal_setting
        except PersonalSetting.DoesNotExist:
            personal_setting = PersonalSetting(user=user)

        return user


class EventList(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    serializer_class = EventSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', '=important_level']
    ordering_fields = ['time']
    
def get_queryset(self):
    user = self.request.user
    all_events = user.event_set.all()

    start_date = self.kwargs.get('start_date', None)
    # convert start date to datetime object
    if start_date:
        all_events.filter(time__gte=start_date)

    end_date = self.kwargs.get('end_date', None)
    # convert start date to datetime object
    if end_date:
        all_events.filter(time__lt=end_date)

    return user.accounts.all()


