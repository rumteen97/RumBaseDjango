from django.contrib.admin import ModelAdmin


class BaseAdmin(ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:  # If the object is being created
            obj.created_by = request.user  # Set the creator
        obj.updated_by = request.user  # Always set the updater
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        base_readonly_fields = [
            'created_at''',
            'updated_at''',
            'created_by''',
            'updated_by''',
        ]  # Fields to be read-only for all models
        readonly_fields = list(base_readonly_fields) + list(self.readonly_fields)
        return readonly_fields
