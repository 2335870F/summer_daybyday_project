from django.contrib import admin
from entries.models import *

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ('name','importance','chef')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', 'type')}

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('entry','author','rating','comment')

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('comment','author')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','email', 'comment')

class ExtraInformationAdmin(admin.ModelAdmin):
    list_display = ('entry','comment')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Chef)
admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ExtraInformation, ExtraInformationAdmin)
