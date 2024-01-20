from django.contrib import admin
from main.models import Education,Qualification,Profile,Message,AcademicProject,AcademicProjectCategory
from django.utils.html import format_html

admin.site.register(Education)
admin.site.register(Qualification)
admin.site.register(AcademicProjectCategory)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','text','date']
    search_fields = ['name','email','text']
    list_filter = ['date']
    list_editable = ['email']
    ordering = ["-date"]
    readonly_fields = ["name",'text']
    date_hierarchy = 'date'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','phone','linkedin','city','image_show']

    @admin.display
    def image_show(self,obj):
        return format_html(f'<img style="height: 100px;" src="{obj.image.url}" />')


@admin.register(AcademicProject)
class AcademicProjectAdmin(admin.ModelAdmin):
    list_display = ['text','date_start','date_end','category','pk']
    list_filter = ['category','date_start','date_end']