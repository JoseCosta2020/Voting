from django.contrib import admin
from .models import Question, Choice

# Register your models here.
admin.site.site_header='The poll mall'
admin.site.site_title ="Voting Admin Area"
admin.site.index_title ="Welcome to our Voting Admin Area"

#COISAS PARA O SUPERUSER PRENNCHER E CRIAR COISAS
class ChoiceInLine(admin.TabularInline):
    model = Choice
    #Tres escolhas somente mas podes adicionar na app extra pode ser outro
    extra = 2
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['question_text']}),
    ('Date Information', {'fields':['pub_date'],'classes':
        ['collapse']}),]
    inlines = [ChoiceInLine]

#Espera um modelo para criar um interface com o nome do modelo
admin.site.register(Question,QuestionAdmin)  
    