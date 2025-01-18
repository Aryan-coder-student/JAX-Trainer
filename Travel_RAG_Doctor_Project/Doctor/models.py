import uuid
import os
from django.contrib.auth.models import User
from django.db import models


def upload_profile_photo(instance, filename):
    """
    Generate file path for new profile photo based on UUID.
    """
    extension = filename.split(".")[-1]
    # File will be uploaded to: 'profile_photos/<uuid>.extension'
    return os.path.join("profile_photos", f"{instance.uuid}.{extension}")


class DoctorProfile(models.Model):
    # UUID for unique identification
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # One-to-one relationship with Django's built-in User model
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="doctor_profile"
    )
    # Basic information
    full_name = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=10,
        choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
    )
    contact_number = models.CharField(max_length=15)
    profile_photo = models.ImageField(
        upload_to=upload_profile_photo, blank=True, null=True
    )
    # Timestamp
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.username})"


class DoctorProfessionalDetail(models.Model):
    # Foreign key relation to DoctorProfile
    doctor_profile = models.OneToOneField(
        DoctorProfile, on_delete=models.CASCADE, related_name="professional_detail"
    )
    # Professional details
    education = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)  # Enter Doctor Name
    registration_number = models.CharField(
        max_length=50, unique=True
    )  # Browse by Registration Number
    year_of_registration = models.IntegerField()  # Browse by Year of Registration
    state_medical_council = models.CharField(max_length=255)  # State Medical Council
    is_verified = models.BooleanField(default=False)  # Verification (via your script)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.doctor_name} ({self.registration_number})"
