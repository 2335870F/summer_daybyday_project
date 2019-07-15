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
	title = forms.CharField(widget=forms.TextInput(),max_length=128, label="Title")
	rating = forms.DecimalField(widget=forms.NumberInput(), min_value=0, max_value=5, required=True, label="Rating 1 to 5")
	comment = forms.CharField(widget=forms.Textarea(),label="Any additional comments")

	class Meta:
		model = Review
		exclude = ('entry','author','date_last_edited')

class SuggestForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(), label="Leave a suggestion for a new cuisine or occasion!", required=False)

	class Meta:
		model = Suggestion
		fields = ('comment',)

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(), label="First name", required=True)
    email = forms.CharField(widget=forms.EmailInput(), label="Email address", required=True)
    comment = forms.CharField(widget=forms.Textarea(), help_text="Leave your comment or question here.", required=True)

    class Meta:
        model = Contact
        fields = ('first_name','email', 'comment')

#asls for name of entry, a photo, and cook time of entry
class AddEntryForm(forms.ModelForm):
    CATEGORIES =(
    ("1","My Courses"),
    ("2","My Work"),
    ("3","My Weekends"),
    ("4","My Holidays"),
    ("6","My Hobbies"),
    ("7","My Home"),
    ("8","Other"),
    ("9","Degree Courses"),
    ("10","Electives"),
    ("11","Grocery Lists"),
    ("12","Personal"),
    ("13","Family"),
    )
    name = forms.CharField(widget=forms.TextInput(), max_length=40, label="Title Your Entry", help_text="up to 40 characters", required=True)
    photo = forms.ImageField(label="Upload a Picture", required=False)
    content = forms.CharField(widget=forms.Textarea(), label="Your Content", required=False)
    importance = forms.IntegerField(min_value=0, max_value=5, initial=0, help_text="1 is least, 5 is most", required=True)
    key_info = forms.CharField(widget=forms.Textarea(), label="Key Information", help_text="e.g. Lecture times, Professor email, etc.", initial="hello", required=False)
    to_do = forms.CharField(widget=forms.Textarea(), label="To-Do", required=False)
    #slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    categories = forms.MultipleChoiceField(widget=forms.SelectMultiple(),choices=CATEGORIES, required=True, help_text="Hold Down Control (Command on Mac) to choose up to three categories!")

    class Meta:
        model = Entry
        fields = ('name','photo','content','importance','key_info','to_do','categories',)

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
    importance = forms.IntegerField(min_value=0, max_value=5, initial=0, help_text="1 is least, 5 is most", required=True)
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
		fields = ('email','first_name','last_name',)

	def clean_password(self):
		return ""

class EditBioForm(UserChangeForm):
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
