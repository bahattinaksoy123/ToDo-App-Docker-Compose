from django.contrib import admin
from django.urls import path
# from django.conf.urls import url
from core import views

urlpatterns = [
    # path('today/', ),
    # path('previous/', ),
    # path('future/', ),
    # path('day/(date)', ),
    path('', views.TodoView.as_view()),
]
    # WORKING PATHS
    # # path('all/', ),
    # path('completed/', ),
    # path('notcompleted/', ),
    # # path('complete/<int:id>', ),
    # # path('uncomplete/<int:id>', ),
    # # path('update-title/<int:id>/<string:title>', ),
    # # path('update-text/<int:id>/<string:text>', ),
    # # path('update-date/<int:id>/<string:date>', ),
    # # path('create/', ),
    # # path('delete/', ),
    # path('<int:id>', views.TodoView.get_one_todo),

