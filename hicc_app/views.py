from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Question, Answer

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'question_detail_ssr.html', {
        'question': question,
        'answers': answers,
    })