### faq app models


from django.db import models
from django.contrib.auth.models import User # so we can associate
from django.utils import timezone  # for tz aware dates
from django.urls import reverse # for category url


class PublishedManager(models.Manager):
    #   custom model manager for question
    #   allows us to default return only records which are published
    def get_queryset(self):
        return super().get_queryset().filter(status=Question.Status.PUBLISHED)

class QuestionCategory(models.Model):
    #   Categories of Questions

    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=75)

    class Meta:
        ordering = ['category']
        indexes = [
            models.Index(fields=['category'])
        ]
        #   for admin names
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        #   model text listing
        return self.category
    
    def get_absolute_url(self):
        return reverse('faq:questions_by_category', args=[self.slug])

class Question(models.Model):
    #   Categories of Questions

    #   enum for status tracking
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"    

    question = models.CharField(max_length=50)
    slug = models.SlugField(max_length=75)
    answer = models.TextField(blank=True)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="questions"
    )

    category = models.ForeignKey(
        #   category
        QuestionCategory,
        on_delete=models.CASCADE,
        related_name="questions",
        null=True,
        blank=True,
    )

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #   track status
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    #   Add custom model manager
    #   Need to declare objects because we want the default way of looking too (get them by obj vs published)
    #   just also want our custom (published)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['question']
        indexes = [
            models.Index(fields=['question'])
        ]

    def __str__(self):
        #   model text listing
        return self.question