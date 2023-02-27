from django.urls import path

from .views import base_views, question_views, answer_views, comment_views

# 네임스페이스 : 앱이 여러개 추가될 경우 url 별칭이 중복 사용될 문제가 생길 경우 중복문제를 해결하기 위해서 사용함
app_name = 'pybo'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'), # '' = pybo/urls.py 자기 자신
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),

    # comment_views.py
    path('comment/create/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),
    path('comment/vote/<int:comment_id>/', comment_views.comment_question_vote, name='comment_question_vote'),
    path('comment/create/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),
    path('comment/vote/<int:comment_id>/', comment_views.comment_answer_vote, name='comment_answer_vote'),
]