### faq app admin


from django.contrib import admin
#   our models
from .models import QuestionCategory, Question


@admin.register(QuestionCategory)
class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
    prepopulated_fields = {'slug': ('category',)}

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'author', "publish", "status"]
    list_filter = ["status", 'category', "publish", "author"]
    prepopulated_fields = {'slug': ('question',)}    
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    list_editable = ['category', 'status']