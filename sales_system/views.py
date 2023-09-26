from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "sales_system/index.html", context)

def cases(request):
    return render(request, "sales_system/cases.html")

def case_detail(request):
    case_id = request.GET.get("case_id")
    case = Cases.objects.get(pk=case_id)
#    case = Cases.objects.get(id=self.kwargs['case_id'])

    return render(request, "sales_system/case_detail.html", {'case': case})