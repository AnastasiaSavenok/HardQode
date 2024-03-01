from rest_framework import serializers

from src.lessons import models


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ('name', 'video_link', 'product')
