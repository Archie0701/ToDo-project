from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',
                    'completed','created_at','due_date',
                    'user'
                    )
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('completed', )
    list_editable = ('completed', )
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'title', 'description', 'completed', 'created_at', 'due_date',)
    readonly_fields = ('id', 'created_at', 'due_date',)


admin.site.register(Task, TaskAdmin)