from django import forms
from entries.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import datetime
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email','first_name','last_name','password')

# our version of UserProfile
class ChefForm(forms.ModelForm):
	photo = forms.ImageField(required=False)
	bio = forms.Textarea()
	class Meta:
		model = Chef
		fields = ('photo','bio')

#asks for title of rating, actual rating 0-5 decimal, and any additional comments
class ReviewForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(),max_length=20, label="Title")
	rating = forms.DecimalField(widget=forms.NumberInput(), min_value=0, max_value=5, required=True, label="Rating 1 to 5")
	comment = forms.CharField(widget=forms.Textarea(),label="Any additional comments")

	class Meta:
		model = Review
		exclude = ('entry','author','date_last_edited')

class ExtraInformationForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(),label="Any additional comments")

	class Meta:
		model = ExtraInformation
		exclude = ('entry','date_last_edited')

class SuggestForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(), label="Can't find the right category to describe your entry? Leave a suggestion for a new category!", required=True)

	class Meta:
		model = Suggestion
		fields = ('comment',)

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(), label="First name", required=True)
    comment = forms.CharField(widget=forms.Textarea(), help_text="Leave your comment or question here & your email address if you want us to get back to you!", required=True)

    class Meta:
        model = Contact
        fields = ('first_name', 'comment')

#asls for name of entry, a photo, and cook time of entry
class AddEntryForm(forms.ModelForm):
    CATEGORIES =(
    ("1","My Courses"),
    ("2","My Work"),
    ("3","My Weekends"),
    ("4","My Holidays"),
    ("5","My Hobbies"),
    ("6","My Home"),
    ("7","Other"),
    ("8","Degree Courses"),
    ("9","Electives"),
    ("10","Grocery Lists"),
    ("11","Personal"),
    ("12","Family"),
    )
    name = forms.CharField(widget=forms.TextInput(), max_length=40, label="Title Your Entry", help_text="up to 40 characters", required=True)
    photo = forms.ImageField(label="Upload a Picture", required=False)
    content = forms.CharField(widget=forms.Textarea(), label="Your Content", required=False)
    importance = forms.IntegerField(label="Priority", min_value=1, max_value=5, initial=1, help_text="1 is first, 5 is last", required=True)
    key_info = forms.CharField(widget=forms.Textarea(), label="Key Information", help_text="e.g. Lecture times, Professor email, etc.", initial="hello", required=False)
    to_do = forms.CharField(widget=forms.Textarea(), label="To-Do", required=False)
    #slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    categories = forms.MultipleChoiceField(widget=forms.SelectMultiple(),choices=CATEGORIES, required=True, help_text="Hold Down Control (Command on Mac) to choose several categories!")

    class Meta:
        model = Entry
        fields = ('name','photo','content','importance','key_info','to_do','categories')

    def save(self, username):
        author = User.objects.get(username=username)
        self.chef = author
        print(self.cleaned_data)
        entry = super(AddEntryForm, self).save(commit=False)
        return entry;



class AddReminderForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), max_length=40, label="Title Your Reminder", help_text="up to 40 characters", required=True)
    photo = forms.ImageField(label="Upload a Picture", required=False)
    content = forms.CharField(widget=forms.Textarea(), label="Your Reminder", required=False)
    importance = forms.IntegerField(label="Priority", min_value=1, max_value=5, initial=1, help_text="1 is first, 5 is last", required=True)
    #slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Reminder
        fields = ('name','photo','content','importance',)

    def save(self, username):
        author = User.objects.get(username=username)
        self.chef = author
        print(self.cleaned_data)
        reminder = super(AddReminderForm, self).save(commit=False)
        return reminder;

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))



class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('first_name','last_name',)

	def clean_password(self):
		return ""

class EditBioForm(UserChangeForm, forms.ModelForm):
    #photo = forms.ImageField(required=False)
    class Meta:
        model = Chef
        fields = ('photo', 'bio')

    def clean_password(self):
        return ""

class EditEntryForm(UserChangeForm):
    class Meta:
        model = Entry
        fields = ('name','photo','key_info','to_do','content','categories','importance')

    def clean_password(self):
        return ""

class EditReminderForm(UserChangeForm):
    class Meta:
        model = Reminder
        fields = ('name','photo','importance','content')

    def clean_password(self):
        return ""

