from django.contrib import admin

from apps.chat.models import Room, Message, UserRoom


class MessageInlineAdmin(admin.TabularInline):
    model = Message
    extra = 1
    max_num = 2

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0

        return self.extra

    def get_max_num(self, request, obj=None, **kwargs):
        return self.max_num


class RoomAdmin(admin.ModelAdmin):
    inlines = [
        MessageInlineAdmin,
    ]
    list_display = ('name', 'label')
    search_fields = ('name', 'label')
    ordering = ('label',)
    fieldsets = (
        ('Room', {'fields': ('name', 'label')}),
    )


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


class UserRoomAdmin(admin.ModelAdmin):
    list_display = ('user', 'room')
    search_fields = ('user__username', 'room__name', 'room__label')
    ordering = ('user', 'room')
    fieldsets = (
        ('User', {'fields': ('user',)}),
        ('Room', {'fields': ('room',)}),
    )


admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(UserRoom, UserRoomAdmin)
