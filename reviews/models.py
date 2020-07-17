from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models


class Review(core_models.TimeStampedModel):

    review = models.TextField()
    accruacy = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    communication = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    cleanliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    location = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    checkin = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user= models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE)
    room= models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review} - {self.room.name}'

    def rating_average(self):
        avg= (
            + self.accruacy
            + self.communication
            + self.cleanliness
            + self.location
            + self.checkin
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description= "Avg."

    class Meta:
        ordering= ('-created',)
