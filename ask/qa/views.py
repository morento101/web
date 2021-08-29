from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.core.paginator import Paginator


def test(request, *args, **kwargs):
	return HttpResponse('OK')


def new_ques(request):
	qa = Question.objects.new()
	limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except Exception:
		page = 1
	paginator = Paginator(qa, limit)
	paginator.baseurl = '/?page='
	try:
		page = paginator.page(page)
	except:
		page = paginator.page(paginator.num_pages)
	return render(request, 'new.html', {
		'qa': page.object_list,
		'paginator': paginator,
		'page': page
	})


def popular(request):
	qa = Question.objects.popular()
	limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except Exception:
		page = 1
	paginator = Paginator(qa, limit)
	paginator.baseurl = '/popular/?page='
	try:
		page = paginator.page(page)
	except:
		page = paginator.page(paginator.num_pages)
	return render(request, 'popular.htlm', {
		'qa': page.object_list,
		'paginator': paginator,
		'page': page
	})


def question(request):
	id = request.GET.get('question_id', None)
	if id is None:
		raise Http404
	qa = Question.objects.get(pk=id)
	ans = qa.answer.all()[:]
	return render(request, 'question.html', {
		'qa': qa,
		'ans': ans
	})
