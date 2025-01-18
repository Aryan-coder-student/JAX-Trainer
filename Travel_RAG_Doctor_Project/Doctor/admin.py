from django.utils.html import format_html
from django.contrib import admin
from .models import DoctorProfile, DoctorProfessionalDetail


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "full_name",
        "gender",
        "contact_number",
        "time_created",
        "profile_photo_preview",
    )

    def profile_photo_preview(self, obj):
        if obj.profile_photo:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; border-radius: 50%;" />',
                obj.profile_photo.url,
            )
        return "No Photo"

    profile_photo_preview.short_description = "Profile Photo"


@admin.register(DoctorProfessionalDetail)
class DoctorProfessionalDetailAdmin(admin.ModelAdmin):
    list_display = (
        "doctor_name",
        "registration_number",
        "year_of_registration",
        "state_medical_council",
        "is_verified",
    )
