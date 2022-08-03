from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import AddPasswordForm, CcDataForm
from .models import GeneralPassword, CardData

@login_required
def dashboard_view(request):
	data = {}

	return render(request, 'pages/dashboard.html', data)

@login_required
def manage_passwords(request):
	# check the request method and then bond the data to forms
	if request.method == 'POST':
		form1 = AddPasswordForm(request.POST)
		form2 = CcDataForm(request.POST)
	elif request.method == 'GET':
		form1 = AddPasswordForm()
		form2 = CcDataForm()
	
	# Query data from database
	recent_passwords = GeneralPassword.objects.filter(user=request.user).filter(delete_pass=False).order_by('-id').all()[:6]
	recent_cc = CardData.objects.filter(user=request.user).filter(delete_card=False).order_by('-id').all()[:6]

	# check the form data, then process the form data
	if form1.is_valid():
		form2 = CcDataForm() # assign the empty form data to form2
		title = form1.cleaned_data.get('title')
		username = form1.cleaned_data.get('username')
		password = form1.cleaned_data.get('password')
		category = form1.cleaned_data.get('category')
		notes = form1.cleaned_data.get('notes')

		data = GeneralPassword(title=title, username=username, password=password, category=category, notes=notes, user=request.user)
		data.save()
		return redirect(reverse('manage-passwords')) # redirect the same page after successful data saving

	# same as the form1 
	if form2.is_valid():
		form1 = AddPasswordForm()
		cc_number = form2.cleaned_data.get('cc_number')
		cc_holder_name = form2.cleaned_data.get('cc_holder_name')
		exp_date = form2.cleaned_data.get('exp_date')
		ccv_code = form2.cleaned_data.get('ccv_code')
		cc_notes = form2.cleaned_data.get('cc_notes')

		data = CardData(cc_number=cc_number, cc_holder_name=cc_holder_name, exp_date=exp_date, ccv_code=ccv_code, cc_notes=cc_notes, user=request.user)
		data.save()
		return redirect(reverse('manage-passwords'))

	data = {'form1': form1, 'form2': form2, 'recent_passwords': recent_passwords, 'recent_cc': recent_cc}
	
	return render(request, 'pages/manage_passwords.html', data)

@login_required
def all_passwords(request):
	if request.method == 'POST':
		search_query = request.POST.get('s_data')
		s_data = GeneralPassword.objects.filter(user=request.user).filter(delete_pass=False).filter(Q(title__icontains=search_query) | Q(username__icontains=search_query))
	else:
		s_data = None

	all_pass = GeneralPassword.objects.filter(user=request.user).filter(delete_pass=False).all().order_by('id')

	paginator = Paginator(all_pass, 12)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	data = {'all_pass': all_pass, 'page_obj': page_obj, 's_data': s_data}

	return render(request, 'pages/all_passwords.html', data)

@login_required
def update_password(request):
	if request.method == 'POST':
		up_data = GeneralPassword.objects.filter(user=request.user).filter(delete_pass=False).get(pk=request.POST.get('up_id'))
	else:
		up_data = None
		
	if request.method == 'POST' and request.POST.get('updata') == 'update':
		title = request.POST.get('title')
		username = request.POST.get('username')
		password = request.POST.get('password')
		category = request.POST.get('category')
		notes = request.POST.get('notes')

		GeneralPassword.objects.filter(pk=request.POST.get('up_id')).update(title=title, username=username, password=password, category=category, notes=notes)

		return redirect(reverse('all-passwords'))
	data = {'up_data': up_data,}

	return render(request, 'pages/update_password.html', data)

@login_required
def delete_password(request):
	if request.method == 'POST':
		GeneralPassword.objects.filter(user=request.user).filter(pk=request.POST.get('del_id')).update(delete_pass=True)

		return redirect(reverse('all-passwords'))

@login_required
def all_cards(request):
	if request.method == 'POST':
		search_query = request.POST.get('s_data')
		s_data = CardData.objects.filter(user=request.user).filter(delete_card=False).filter(Q(cc_holder_name__icontains=search_query) | Q(cc_number__icontains=search_query))
	else:
		s_data = None

	all_cards = CardData.objects.filter(user=request.user).filter(delete_card=False).all().order_by('id')

	paginator = Paginator(all_cards, 12)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	data = {'all_cards': all_cards, 'page_obj': page_obj, 's_data': s_data}

	return render(request, 'pages/all_cards.html', data)

@login_required
def update_card(request):
	if request.method == 'POST':
		up_data = CardData.objects.filter(user=request.user).filter(delete_card=False).get(pk=request.POST.get('up_id'))
	else:
		up_data = None
		
	if request.method == 'POST' and request.POST.get('updata') == 'update':
		cc_number = request.POST.get('cc_number')
		cc_holder_name = request.POST.get('cc_holder_name')
		exp_date = request.POST.get('exp_date')
		ccv_code = request.POST.get('ccv_code')
		cc_notes = request.POST.get('cc_notes')

		CardData.objects.filter(pk=request.POST.get('up_id')).update(cc_number=cc_number, cc_holder_name=cc_holder_name, exp_date=exp_date, ccv_code=ccv_code, cc_notes=cc_notes)

		return redirect(reverse('all-cards'))
	data = {'up_data': up_data,}

	return render(request, 'pages/update_card.html', data)

@login_required
def delete_card(request):
	if request.method == 'POST':
		CardData.objects.filter(user=request.user).filter(pk=request.POST.get('del_id')).update(delete_card=True)
		return redirect(reverse('all-cards'))

@login_required
def all_trash(request):
	trash_pass = GeneralPassword.objects.filter(Q(user=request.user) & Q(delete_pass=True)).order_by('id').all()
	trash_card = CardData.objects.filter(Q(user=request.user) & Q(delete_card=True)).all()

	# deleted password pagination
	paginator = Paginator(trash_pass, 2)
	page_number = request.GET.get('pass-page')
	pass_page_obj = paginator.get_page(page_number)

	# deleted cards pagination
	paginator = Paginator(trash_card, 2)
	page_number = request.GET.get('card-page')
	card_page_obj = paginator.get_page(page_number)
	
	data = {
		'trash_card': trash_card, 'trash_pass': trash_pass, 
		'pass_page_obj': pass_page_obj, 'card_page_obj': card_page_obj
		}

	return render(request, 'pages/all_trash.html', data)

@login_required
def restore_pass(request, pass_id):
	GeneralPassword.objects.filter(user=request.user).filter(id=pass_id).update(delete_pass=False)

	return redirect(reverse('all-trash'))

@login_required
def restore_card(request, card_id):
	CardData.objects.filter(user=request.user).filter(id=card_id).update(delete_card=False)

	return redirect(reverse('all-trash'))

