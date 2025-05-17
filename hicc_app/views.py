from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Question, Answer

def question_detail(request, question_id):
    if request.method == 'GET':
        question = Question.objects.get(id=question_id)

        question_data = {
            'id': question.id,
            'subject': question.subject,
            'content': question.content,
            'create_date': question.create_date
        }
        # question이라는 객체의 변수들을 딕셔너리 형식으로 변환하는 과정

        return JsonResponse(question_data)

def answers(request,question_id) :
    if request.method == 'GET':
        answers = list(Answer.objects.filter(question=question_id).values('id', 'question_id', 'content', 'create_date'))
        # 모든 답변 데이터를 가져올건데, objects.all()이 아닌 objects.filter(question = 	question_id)는 인자로 받는 question_id와 id가 일치하는 question들의 답변 데이터만 	가져온다는 의미

        return JsonResponse({'answers': answers})

def questions(request):
    if request.method == 'GET':
        questions = list(Question.objects.all().values('id', 'subject', 'content', 'create_date'))
        return JsonResponse({'questions': questions})  # json 형식으로 설정 후 response

