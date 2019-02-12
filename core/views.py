from django import forms
from django.shortcuts import render, redirect

# Create your views here.
from core.models import Entity, Evaluation, Question


def index(request):
    class EntityForm(forms.Form):
        entity_name = forms.ModelChoiceField(queryset=Entity.objects.all())

    if request.method == 'POST':
        form = EntityForm(request.POST)
        if form.is_valid():
            print("Valid form!")
            print(form.cleaned_data['entity_name'])
            return redirect(entity_view, form.cleaned_data['entity_name'])
    else:  # GET request method
        form = EntityForm()
        return render(request, 'home.html', {'form': form})


def entity_view(request, entity_name):
    entity = Entity.objects.get(entity_name=entity_name)
    evaluation_mcvp = Evaluation.objects.get(type=1, entity=entity)
    evaluation_lcp = Evaluation.objects.get(type=2, entity=entity)
    questions_mcvp = Question.objects.filter(evaluation=evaluation_mcvp)
    score_mcvp = questions_mcvp.values('score')
    questions_lcp = Question.objects.filter(evaluation=evaluation_lcp)
    context_dictionary = {'entity': entity,
                          'evaluation_mcvp': evaluation_mcvp,
                          'evaluation_lcp': evaluation_lcp,
                          'questions_mcvp': questions_mcvp,
                          'score_mcvp': score_mcvp,
                          'questions_lcp': questions_lcp
                          }
    return render(request, 'index.html', context_dictionary)
