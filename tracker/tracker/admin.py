from django.contrib import admin
from .models import Device, Log


class LogAdmin(admin.ModelAdmin):
    list_display = ('device', 'get_user_username', 'get_user_name', 'get_device_name', 'timestamp')

    def get_user_username(self, obj):
        return obj.device.user.username
    get_user_username.short_description = 'User Username'
    get_user_username.admin_order_field = 'device__user__username'

    def get_user_name(self, obj):
        return obj.device.user.name
    get_user_name.short_description = 'User Name'
    get_user_name.admin_order_field = 'device__user__name'

    def get_device_name(self, obj):
        return obj.device.name
    get_device_name.short_description = 'Device Name'
    get_device_name.admin_order_field = 'device__name'

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'mac_address', 'type')
    list_filter = ('type', 'user')
    search_fields = ('name', 'mac_address', 'user__username', 'user__name')
    autocomplete_fields = ['user']


admin.site.register(Log, LogAdmin)
admin.site.register(Device, DeviceAdmin)
