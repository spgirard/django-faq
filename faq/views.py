### faq app views


from django.shortcuts import render
#   bring in models
from .models import Question, QuestionCategory
#   for db requests
from django.shortcuts import render, get_object_or_404

def list(request, category_slug=None):
    #   default 'all' list
    #   or by passed category slug
    questions = Question.published.all()
    categories = QuestionCategory.objects.all()
    category = None

    if category_slug:
        category = get_object_or_404(QuestionCategory, slug=category_slug)
        questions = Question.published.filter(category=category)

    context = {
        'category': category,
        'questions': questions,
        'categories': categories,
    }
    return render(request, 'faq/index.html', context)
