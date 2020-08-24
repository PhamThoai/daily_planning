from django.contrib import admin
from .models import (
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
# Register your models here.

admin.site.register(PersonalSetting)
admin.site.register(Evaluation)
admin.site.register(LongTermPlan)
admin.site.register(LongTermProcessEvaluation)
admin.site.register(ShortTermPlan)
admin.site.register(ShortTermProcessEvaluation)
admin.site.register(Event)
admin.site.register(PlanForDay)
admin.site.register(EvaluationForDay)