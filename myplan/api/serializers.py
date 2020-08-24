from rest_framework import serializers
from myplan.models import (
    PersonalSetting,
    Evaluation,
    LongTermPlan,
    LongTermProcessEvaluation,
    ShortTermPlan,
    ShortTermProcessEvaluation,
    Event,
    PlanForDay,
    EvaluationForDay
)


# Serializers for PersonalSetting

class PersonalSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalSetting
        fields = '__all__'


# Serializers for Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


# Serializers for PlanForDay

class PlanForDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanForDay
        fields = '__all__'


# Serializers for EvaluationForDay

class EvaluationForDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationForDay
        fields = '__all__'


# Serializers for Evaluation

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'


# Serializers for LongTermPlan

class LongTermPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LongTermPlan
        fields = '__all__'


# Serializers for ShortTermPlan

class ShortTermPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortTermPlan
        fields = '__all__'