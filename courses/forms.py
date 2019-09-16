from django.forms import forms

from . import models


class QuizForm(forms.Form):
    class Meta:
        model = models.Quiz
        fields = [
            'title',
            'description',
            'order',
            'total_questions',
        ]


class TrueFalseQuestionForm(forms.Form):
    class Meta:
        model = models.TrueFalseQuestion
        fields = [
            'order',
            'prompt',
        ]


class MultipleChoiceQuestionForm(forms.Form):
    class Meta:
        model = models.TrueFalseQuestion
        fields = [
            'order',
            'prompt',
            'shuffle_answers'
        ]