from django.contrib import admin

from .models import Question,Choice

# customizing the admin form look and feel

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None, { 'fields' : ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)

