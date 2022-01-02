from django.db import models

from . import utils
from .user import User

class GenderEnum(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"
    OTHER = "O", "Other"


class Profile(utils.CustomModel):
    address = models.TextField()
    phone = models.TextField()
    gender = models.CharField(
        max_length=1,
        choices=GenderEnum.choices,
        default=GenderEnum.MALE,
    )
    age = models.IntegerField()
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        db_column="userId",
        related_name="profiles",
        related_query_name="profile",
        unique=True
    )
    createdAt = models.DateTimeField(auto_now_add=True, db_index=True)
    updatedAt = models.DateTimeField(auto_now=True)