from django.db import models

TYPE_CHOICES = (
    (1, 'MCVPs'),
    (2, 'LCPs')
)


class Entity(models.Model):
    entity_name = models.CharField(max_length=128)
    region_name = models.CharField(max_length=128)
    mcp_name = models.CharField(max_length=128)

    def __str__(self):
        return self.entity_name


class Evaluation(models.Model):
    type = models.IntegerField(choices=TYPE_CHOICES)
    number_of_responses = models.IntegerField(default=0)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)


class Question(models.Model):
    question_text = models.CharField(max_length=500)
    score = models.FloatField(default=0.0)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
