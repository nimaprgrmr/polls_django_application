from django.contrib import admin
from .models import Question, Choice


# admin.site.register(Question)

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"] #‌this use for set ordinary of fields in QuestionAdmin 

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["question_text"]}),
#         ("Date information", {"fields": ["pub_date"]}),
#     ]

# admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

class ChoiceInline(admin.TabularInline): #‌ for change the view of show choices in admin page, it is very smaller and more readble
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin): #‌ show the Choices in Question 
    fieldsets = [
        (None, {"fields": ["question_text"],}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"] #‌ this is for adding filter pub_date in admin panel for show what questions??‌today uploaded?‌ last week uploaded?‌or ..
    search_fields = ["question_text"] #‌ For adding search box to admin panel for questions 
    

admin.site.register(Question, QuestionAdmin)
