from django.shortcuts import render

# Create your views here.
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
        # question이라는 객체의 변수들을 딕셔너리 형식으로 변환하는 직렬화 과정

        return JsonResponse(question_data) # 이미 위에서 직렬화가 끝난게 question_data이므로 그대로 반환


def questions(request):
    if request.method == 'GET':
        questions = Question.objects.all().values('id', 'subject', 'content', 'create_date')
        return JsonResponse({'questions': list(questions)})

def answers(request,question_id) :
    if request.method == 'GET':
        answers = list(Answer.objects.filter(question=question_id).values('id', 'question_id', 'content', 'create_date'))
        #Answer 클래스에서 url에 있는 question_id 값과 일치하는 질문들만 전부 가져오는데, 각각 'id', 'question_id', … 등의 이름으로 가져옴, 그 후 list 형식으로 변환
        return JsonResponse({'answers': answers}) # answers는 list 값이기 때문에 직렬화 필요. 'answers' : 로 직렬화 해줌

