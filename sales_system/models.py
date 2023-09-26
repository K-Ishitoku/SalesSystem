from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
class Vendors(models.Model):
    company_name = models.CharField(max_length=200)

class Cases(models.Model):
    #ベンダーを削除するとそのベンダーの案件も削除される
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    source = models.CharField(max_length=200, blank=True)
    sap_flg = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    #blank=TrueでNOT NULLを外す
    industry = models.CharField(max_length=200, blank=True)
    cost_lower = models.CharField(max_length=200, blank=True)
    cost_upper = models.CharField(max_length=200, blank=True)
    settlement = models.CharField(max_length=200, blank=True)
    role_overview = models.CharField(max_length=200, blank=True)
    details = models.CharField(max_length=200, blank=True)
    essential_skills = models.CharField(max_length=200, blank=True)
    preferred_skills = models.CharField(max_length=200, blank=True)
    age_limit = models.IntegerField(null=True, blank=True)
    sales_restricions = models.CharField(max_length=200, blank=True)
    english_skills = models.CharField(max_length=200, blank=True)
    foreign_nationality = models.CharField(max_length=200, blank=True)
    work_location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    working_conditions = models.CharField(max_length=200, blank=True)
    pic = models.CharField(max_length=200, blank=True)
    contract_terms = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    registant = models.CharField(max_length=200, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updater = models.CharField(max_length=200, blank=True)
    remarks = models.CharField(max_length=200, blank=True)
    