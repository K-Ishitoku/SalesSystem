from django.urls import path
from . import views

urlpatterns = [
    # ex: /sales_system/
    path("", views.index, name = "index"),
    # # ex: /sales_system/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # # ex: /sales_system/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /sales_system/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
    path("cases/", views.cases, name="cases"),
    path("case_detail/", views.case_detail, name="case_detail"),
]