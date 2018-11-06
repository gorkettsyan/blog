from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Writing
from .forms import WritingCreateForm
from django.core.urlresolvers import reverse
from django.shortcuts import  get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def writing_listview(request):
	template_name = 'writings/writing_list.html'
	writings = Writing.objects.all()

	paginator = Paginator(writings, 10)
	page = request.GET.get('page')
	try:
		writingpage = paginator.page(page)
	except PageNotAnInteger:
		writingpage = paginator.page(1)
	except EmptyPage:
		writingpage = paginator.page(paginator.num_pages)

	context = {
				'writingpage':writingpage
		}

	return render(request, template_name, context)







def writing_createview(request):
	template_name = 'writings/writing_create_form.html'
	form = WritingCreateForm()

	if request.method == 'POST':
		form = WritingCreateForm(request.POST or None)
		if request.user.is_authenticated():

			if form.is_valid():
				instance = form.save(commit=False)
				instance.owner = request.user
				instance.save()
				return HttpResponseRedirect(reverse("writings:detail", kwargs={'pk': instance.pk}))
			else:
				form = WritingCreateForm()
		else:
			return redirect(reverse("accounts:login"))

	context = {
			'form': form
		}

	return render(request,template_name, context)




def writing_detailview(request, pk):
	template_name = "writings/writing_detail.html"
	queryset = get_object_or_404(Writing, pk=pk)

	context = {
		'object' : queryset,
	}
	return render(request, template_name, context)


class WritingEdit(UpdateView):
	model = Writing
	fields = ['title','body', 'category']
	template_name_suffix = '_update'
