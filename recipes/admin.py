from django.contrib import admin
from recipes.models import UserProfile
from recipes.models import Category, Recipe

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_categories', 'description')  # Fields to display in the list view
    filter_horizontal = ('categories',) # add and remove of categories
    
    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    get_categories.short_description = 'Categories'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(UserProfile)


