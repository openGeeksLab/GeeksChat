from django.contrib import admin

from apps.chat.models import Room, Message


class MessageInlineAdmin(admin.TabularInline):
    model = Message
    extra = 1

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0

        return self.extra


class RoomAdmin(admin.ModelAdmin):
    inlines = (MessageInlineAdmin,)
    list_display = ('__str__',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'room', 'formatted_timestamp')
    readonly_fields = ('timestamp', 'formatted_timestamp')
    search_fields = ('room__name', 'room__label', 'user__username', 'message')
    ordering = ('room__name', '-timestamp')
    fieldsets = (
        ('Room', {'fields': ('room',)}),
        ('User', {'fields': ('user',)}),
        ('Message', {'fields': ('message', 'formatted_timestamp')}),
    )


admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
