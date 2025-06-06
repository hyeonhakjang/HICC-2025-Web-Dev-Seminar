from django.shortcuts import render
from django.http import HttpResponse

def html_test_render(request) :
    return render(request, 'html 테스트.html')

def image_tag_render(request) :
    return render(request, '이미지 태그.html')

def text_tag_render(request) :
    return render(request, '텍스트 태그.html')

def table_tag_render(request) :
    return render(request, '테이블 태그.html')

def form_tag_render(request) :
    return render(request, '폼 태그.html')

def layout_tag_render(request) :
    return render(request, '레이아웃 태그.html')

def http_test(request):
    return HttpResponse("안녕하세요 hicc 세미나에 오신 것을 환영합니다.")
