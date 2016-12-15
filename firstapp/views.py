from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect

from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core import serializers
from django.conf import settings

import os

from .models import Question

class IndexView(generic.ListView):
	template_name = 'firstapp/home.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')

class crud():
	def savedata(request):
		# model = Question
		# template_name = 'firstapp/results.html'
		sv = Question(name=request.POST['name'], question_text=request.POST['questiontext'], file=request.FILES['file'], image=request.FILES['image'], pub_date=timezone.now())
		sv.save()
		# return redirect()

		return HttpResponseRedirect(reverse('firstapp:index'))

	def editdata(request, data_id):
		# data = Question.objects.get(id=data_id)
		# return HttpResponse(dt)
		data = get_object_or_404(Question, pk=data_id)
		# return HttpResponse(data)
		alldata = Question.objects.order_by('-pub_date') #serializers.deserialize('json', Question.objects.all())
		# return render_to_response('firstapp/home.html', {'data': data, 'qid' : data_id, 'getdata' : alldata})
		return render(request, 'firstapp/home.html', {'data': data, 'qid' : data_id, 'getdata' : alldata})

	def updatedata(request):
		ed = Question.objects.get(id=request.POST['qid'])
		
		#return HttpResponse(settings.MEDIA_ROOT+'/'+ed.image.name.replace('/', '\\'))

		imagePath = os.path.join(settings.MEDIA_ROOT, ed.image.name)
		filePath = os.path.join(settings.MEDIA_ROOT, ed.file.name)

		if 'image' in request.FILES:
			ed.image = request.FILES['image']
			if os.path.isfile(imagePath):
				os.remove(imagePath)

		if 'file' in request.FILES:
			ed.file = request.FILES['file']
			if os.path.isfile(filePath):
				os.remove(filePath)

		ed.name=request.POST['name']
		ed.question_text=request.POST['questiontext']
		ed.save()

		return HttpResponseRedirect(reverse('firstapp:index'))

	def deletedata(request, data_id):
		dl = Question.objects.get(id=data_id)

		imagePath = os.path.join(settings.MEDIA_ROOT, dl.image.name)
		filePath = os.path.join(settings.MEDIA_ROOT, dl.file.name)

		if os.path.isfile(imagePath):
			os.remove(imagePath)

		if os.path.isfile(filePath):
			os.remove(filePath)

		dl.delete()

		return HttpResponseRedirect(reverse('firstapp:index'))

