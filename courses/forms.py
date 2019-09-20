from django.forms import ModelForm, forms
from django.forms import modelformset_factory, inlineformset_factory

from . import models


class QuizForm(ModelForm):
    class Meta:
        model = models.Quiz
        fields = [
            'title',
            'description',
            'order',
            'total_questions'
        ]


class TrueFalseQuestionForm(ModelForm):
    class Meta:
        model = models.TrueFalseQuestion
        fields = [
            'order',
            'prompt'
        ]


class MultipleChoiceQuestionForm(ModelForm):
    class Meta:
        model = models.MultipleChoiceQuestion
        fields = [
            'order',
            'prompt',
            'shuffle_answers'
        ]


class AnswerForm(ModelForm):
    class Meta:
        model = models.Answer
        fields = [
            'order',
            'text',
            'correct'
        ]


AnswerFormSet = modelformset_factory(
    model=models.Answer,
    form=AnswerForm,
    extra=2
)


AnswerInlineFormSet = inlineformset_factory(
    models.Question,
    models.Answer,
    extra=2,
    fields=('order', 'text', 'correct'),
    formset=AnswerFormSet,
    min_num=1
)
