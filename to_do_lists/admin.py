from src.settings import DEBUG

if DEBUG:
    from django.contrib import admin

    # Register your models here.
    from to_do_lists.models import Task, List, Category


    class CategoryAdmin(admin.ModelAdmin):
        list_display = ["__str__", "user"]
        list_display_links = ["__str__"]
        list_filter = ["__str__", "user"]

        search_fields = ["name", "user"]

        class Meta:
            model = Category


    class ListAdmin(admin.ModelAdmin):
        list_display = ["__str__", "category", "calendar", "user"]
        list_display_links = ["__str__"]
        list_filter = ["category", "user"]

        search_fields = ["name", "description"]

        class Meta:
            model = List


    class TaskAdmin(admin.ModelAdmin):
        list_display = ["__str__", "complete", "due_date", "get_category", "list", "user"]
        list_display_links = ["__str__"]
        list_filter = ["creation_date", "due_date"]
        list_editable = ["complete"]

        search_fields = ["name", "description"]

        class Meta:
            model = Task

    admin.site.register(Task, TaskAdmin)
    admin.site.register(List, ListAdmin)
    admin.site.register(Category)
