from django.contrib import admin
from .models import Question, Choice

# Now we can view some of the models that we created
# admin.site.register([Question, Choice])


class ChoicesInLine(admin.StackedInline):
    model = Choice
    can_delete = False
    verbose_name_plural = 'choices'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ('pub_date',)
    search_fields = ('question_text',)
    inlines = [ChoicesInLine]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes')
    list_filter = ('question',)
    search_fields = ('choice_text',)
