from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from entries.models import *
from entries.forms import *
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import UploadFileForm
from django.shortcuts import get_object_or_404




# Create your views here.


def handle_uploaded_file(f):
    with open('entries/uploads.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
            
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse('index'))
        else:
            form = UploadFileForm()
        return render(request, 'entries/upload.html', {'form':form})
cats_bar = Category.objects.exclude(name__in=['Other Courses','Special Occasions']).order_by('name')

@login_required
def index(request):
	#get all entries, order alphabetically by name - is recent
	latest = Entry.objects.order_by('-date_last_edited')[:4]
	#get all categories -- no order
	reminders = Reminder.objects.order_by('-importance')[:4]
    
	top = Entry.objects.order_by('-importance')[:6]

	context_dict = {'latest':latest, 'reminders':reminders, 'top':top}
	response = render(request,'entries/index.html', context=context_dict)
	return response

def about(request):
	#get users that are chefs -- order alphabetically by username
	chefs = Chef.objects.all()
	context_dict = {'chefs':chefs}

	response = render(request,'entries/about.html', context=context_dict)
	return response

def faq(request):
	return render(request,'entries/faq.html', {})
@login_required
def widgets(request):
	return render(request,'entries/widgets.html', {})
@login_required
def categories(request):
	#get all categories -- no order
	cats = Category.objects.all()
	context_dict = {'cats':cats}
	response = render(request,'entries/categories.html', context=context_dict)
	return response

def register(request):
	registered = False
	if request.method=='POST':
		user_form = UserForm(data=request.POST)
		profile_form = ChefForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			if 'photo' in request.FILES:
				profile.photo = request.FILES['photo']
			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = ChefForm()
	return render(request, 'entries/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		print(user)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your Rango account is disabled.")
		else:
			print("Invalid login details: {0},{1}".format(username, password))
			return HttpResponseRedirect(reverse('invalidlogin'))
	else:
		return render(request, 'entries/login.html', {})

def invalidlogin(request):
	return render(request,'entries/invalidlogin.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

@login_required
def suggestion(request):
	form = SuggestForm()
	if request.method == 'POST':
		form = SuggestForm(data=request.POST)
		if form.is_valid():
			suggestion = form.save(commit=False)
			suggestion.author = request.user
			suggestion.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		print(form.errors)
	return render(request, 'entries/suggestion.html', {'form':form})

def contact(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(data=request.POST)
		if form.is_valid():
			suggestion = form.save(commit=True)
			return HttpResponseRedirect(reverse('index'))
		else:
			print(form.errors)
	return render(request, 'entries/contact.html', {'form':form})

@login_required
def addentry(request):
	form = AddEntryForm(request.FILES)
	if request.method == 'POST':
		form = AddEntryForm(request.POST, request.FILES)
		if form.is_valid():
			entry = form.save(request.user.username)
			entry.chef = request.user
			cats = form.cleaned_data.get('categories')
			if(len(cats) > 3):
				raise forms.ValidationError("You can't select more than 3 items.")
			else:
				entry.save()
				for cat in cats:
					category = Category.objects.get(id=cat)
					entry.categories.add(category)
			entry.save()
			return HttpResponseRedirect(reverse('index'))
		else:
			print(form.errors)
	return render(request, 'entries/addentry.html', {'form':form})

@login_required
def viewentry(request, entry_name_slug):
    context_dict = {'cats_bar':cats_bar}
    try:
        entry = Entry.objects.get(slug=entry_name_slug)
        reviews = Review.objects.filter(entry=entry).order_by("-date_last_edited")
        extrainformation = ExtraInformation.objects.filter(entry=entry).order_by("-date_last_edited")

        if len(reviews) > 0:
            avgRating = (Review.objects.filter(entry=entry).aggregate(Sum('rating'))["rating__sum"])/len(reviews)
            context_dict['avgRating'] = round(avgRating,2)
        else:
            context_dict['avgRating'] = "No rating yet."


        context_dict['entry'] = entry
        context_dict['reviews'] = reviews
        context_dict['extrainformation'] = extrainformation
    except:
        context_dict['entry'] = None

    if request.user.is_authenticated():
        form = ReviewForm()
        form2 = ExtraInformationForm()
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            form2 = ExtraInformationForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.entry = entry
                review.author = request.user
                review.save()
                return redirect('/entries/entry/'+entry_name_slug)
            if form2.is_valid():
                extrainformation = form2.save(commit=False)
                extrainformation.entry = entry
                extrainformation.save()
                return redirect('/entries/entry/'+entry_name_slug)
        else:
            print(form.errors)


        context_dict["form"] = form
        context_dict["form2"] = form2
    return render(request, 'entries/entry.html', context_dict)










@login_required
def addreminder(request):
    form = AddReminderForm(request.FILES)
    if request.method == 'POST':
        form = AddReminderForm(request.POST, request.FILES)
        if form.is_valid():
            reminder = form.save(request.user.username)
            reminder.chef = request.user
            reminder.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    return render(request, 'entries/addreminder.html', {'form':form})

@login_required
def viewreminder(request, reminder_name_slug):
    context_dict = {'cats_bar':cats_bar}
    try:
        reminder = Reminder.objects.get(slug=reminder_name_slug)
        context_dict['reminder'] = reminder
    except:
        context_dict['reminder'] = None

    return render(request, 'entries/reminders.html', context_dict)


def userprofile(request, username):
	context_dict = {}
	try:
		user = User.objects.get(username=username)
		chef = Chef.objects.get(user=user)
		entries = Entry.objects.filter(chef=user)
		reviews = Review.objects.filter(author=user)
		context_dict['reviews'] = reviews
		context_dict['entries'] = entries
		context_dict['chef'] = chef
	except:
		context_dict['chef'] = None

	return render(request, 'entries/profile.html', context_dict)

@login_required
def edit_profile(request, username):
	if request.method == 'POST':
		edit = EditProfileForm(request.POST, request.FILES, instance=request.user)
		bio  = EditBioForm(request.POST, request.FILES, instance=request.user.chef)
		if edit.is_valid() and bio.is_valid():
			edit.save()
			bio.save()
			return redirect('/entries/profile/'+username)
		else:
			print(edit.errors, bio.errors)
	else:
		edit = EditProfileForm(request.FILES, instance=request.user)
		bio = EditBioForm(request.FILES, instance=request.user.chef)

	context_dict = {'edit':edit,'bio':bio}
	return render(request, 'entries/edit_profile.html', context_dict)









@login_required
def change_password(request, username):
	if request.method=='POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('index')
		else:
			print("Passwords did not match.")
	else:
		form=PasswordChangeForm(data=request.POST, user=request.user)
	context_dict = {'form':form}

	return render(request, 'entries/change_password.html', context_dict)

@login_required
def show_category(request, cat_name_slug):
	context_dict = {}

	try:
		cat = Category.objects.get(slug=cat_name_slug)
		entries = cat.entry_set.all()
		subcats = Category.objects.filter(supercat=cat)
		context_dict['entries'] = entries
		context_dict['subcats'] = subcats
		context_dict['cat'] = cat
		context_dict['cats_bar'] = cats_bar
	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['entries'] = None

	return render(request, 'entries/category.html', context_dict)
