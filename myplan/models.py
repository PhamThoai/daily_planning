from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class PersonalSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personal_setting')
    daily_planning_reminder = models.BooleanField(default=True)
    daily_activity_review_reminder = models.BooleanField(default=True)
    

class Evaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    evaluation_content = models.CharField(max_length=255)
    evaluation_note = models.CharField(max_length=120)
    remind_note = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name() + ' : ' + self.evaluation_content


class LongTermPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    start_date = models.DateField(default=now)
    expected_end_date = models.DateField(null=True)
    process_evaluation = models.ManyToManyField(Evaluation, through='LongTermProcessEvaluation')

    def __str__(self):
        return self.user.get_full_name() + ' : ' + self.title


class LongTermProcessEvaluation(models.Model):
    plan = models.ForeignKey(LongTermPlan, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=now)


class ShortTermPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    start_date = models.DateField(default=now)
    expected_end_date = models.DateField(null=True)
    longterm_plan = models.ForeignKey(LongTermPlan, on_delete=models.CASCADE, null=True, blank=True)
    process_evaluation = models.ManyToManyField(Evaluation, through='ShortTermProcessEvaluation')

    def __str__(self):
        return self.user.get_full_name() + ' : ' + self.title


class ShortTermProcessEvaluation(models.Model):
    plan = models.ForeignKey(ShortTermPlan, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=now)


class Event(models.Model):
    NOT_IMPORTANT = 'NI'
    IMPORTANT = 'I'
    VERY_IMPORTANT = 'VI'
    IMPORTANT_CHOICES = (
        (NOT_IMPORTANT, 'NotImportant'),
        (IMPORTANT, 'Important'),
        (VERY_IMPORTANT, 'VeryImportant'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    time = models.DateTimeField()
    event_note = models.CharField(max_length=255)
    important_level = models.CharField(max_length=2, choices=IMPORTANT_CHOICES, default=NOT_IMPORTANT)

    def __str__(self):
        return self.user.get_full_name() + ' : ' + self.titlee


class PlanForDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    start_time = models.TimeField(default=now)
    end_time = models.TimeField(null=True)
    finished = models.BooleanField(default=False)
    in_date = models.DateField(default=now)
    plan = models.ForeignKey(ShortTermPlan, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() + ' : ' + self.title


class EvaluationForDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    evaluation = models.OneToOneField(Evaluation, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.get_full_name() + ' : ' + self.date.__str__() + ' : ' + self.evaluation.evaluation_content
