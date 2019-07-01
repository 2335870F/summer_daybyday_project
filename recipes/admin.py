from django.contrib import admin
from recipes.models import *

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name','cook_time','chef')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', 'type')}

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('recipe','author','rating','comment')

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('comment','author')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('comment','first_name','last_name','email')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Chef)
admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Review, ReviewAdmin)
