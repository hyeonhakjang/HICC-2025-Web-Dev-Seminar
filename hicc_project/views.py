from django.shortcuts import render


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
