from django.shortcuts import render, redirect, render_to_response
from writings.models import Writing
from .forms import RegisterUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from accounts.models import User
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import UpdateView




def user_registerview(request):
	form = RegisterUserForm()
	if request.user.is_authenticated():
		return HttpResponse('You are already registered')

	if request.method == 'POST':
		form = RegisterUserForm(request.POST, request.FILES or None)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(form.cleaned_data['password1'])
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your Writy account.'
			message = render_to_string('accounts/acc_active_email.html', {
				'user': user,
	            'domain': current_site.domain,
	            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
	            'token':account_activation_token.make_token(user),
	        })
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
	                    mail_subject, message, to=[to_email]
	        )
			email.send()
			return HttpResponse('Check your email')



	context = {'form': form}
	template_name = "accounts/register.html"
	return render(request, template_name,context)


def activate(request, uidb64, token):
	User = get_user_model()
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return HttpResponse('Thank You, You account is activated')
	else:
		return HttpResponse('Activation link is invalid!')


def profile_listview(request):
	template_name = "accounts/profile_list.html"

	users = User.objects.all()
	index = 0
	user_list = []
	user_list.append([])

	for idx, usr in enumerate(users):
			user_list[index].append(usr)
			if len(user_list[index]) == 3:
				user_list.append([])
				index = index + 1



	context = {
			'user_list': user_list }


	return render(request, template_name, context)


def profile_detailview(request, user_id):
	template_name = 'accounts/profile_detail.html'
	usr 		  =  get_object_or_404(User, pk=user_id)
	context = {
				'usr':usr
				}
	return render(request, template_name, context)


def profile_detail_writings(request, pk):

	usr = get_object_or_404(User, pk=pk)
	template_name = "accounts/profile_detail_writings.html"
	writing = Writing.objects.filter(owner = usr)

	paginator = Paginator(writing, 10)
	page = request.GET.get('page')
	try:
		writingpage = paginator.page(page)
	except PageNotAnInteger:
		writingpage = paginator.page(1)
	except EmptyPage:
		writingpage = paginator.page(paginator.num_pages)


	context={
		'usr': usr,
		'page': page,
		'writingpage':writingpage
	}
	return render(request, template_name, context)


class ProfileEdit(UpdateView):
	 model = User
	 fields = ['username', 'first_name', 'last_name', 'gender', 'location', 'birth_date', 'picture']
	 template_name_suffix = '_update'
