from django.shortcuts import render
from django.http import HttpResponse

questions = {
    "친구1" :
    {
        1 : "배가고파요.",
        2 : "장고 재밌어요.",
        3 : "이런식이면 디비도?",
        4 : "책 읽는건 싫어요.",
        5 : "빨리 더 잘하고 싶어요",
        6 : "아 재밌어"
    },
    "친구2" :
    {
        1 : "배가고파요. 22",
        2 : "장고 재밌어요. 22",
        3 : "이런식이면 디비도? 22",
        4 : "책 읽는건 싫어요. 22",
        5 : "빨리 더 잘하고 싶어요 22",
        6 : "아 재밌어 22"
    }
}

# Create your views here.
def one_question(request, student_id, questionNum):
    return HttpResponse(f'학생이름:{student_id} <br/> 질문 : {questions.get(student_id, {}).get(questionNum)} <br/> 이렇게 하면 db도 활욜해서 더 재밌어 지겠다!!!')

def main(request):
    return HttpResponse("질문내용을 검색하세요.")