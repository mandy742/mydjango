from django.db import models


# Creating models here.
class Biography(models.Model):
    """
    Model representing a candidate's biography.

    Attributes:
        name (str): The candidate's name.
        date_of_birth (date): The candidate's date of birth.
        place_of_birth (str): The place where the candidate was born.
        education (str): The candidate's educational background.
        events (str): Significant events in the candidate's life.
        achievements (str): The candidate's achievements.
    """
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    education = models.TextField()
    events = models.TextField()
    achievements = models.TextField()
 
    def __str__(self):
        return f"{self.name}'s Biography"

  
class Endorse(models.Model):
    """
    Model representing an endorsement for a candidate.

    Attributes:
        endorser_name (str): The name of the person endorsing the candidate.
        endorser_title (str): The title of the endorser (optional).
        endorsement_text (str): The text of the endorsement.
        date (date): The date of the endorsement.
    """
    endorser_name = models.CharField(max_length=255)
    endorser_title = models.CharField(max_length=255, blank=True, null=True)
    endorser_text = models.TextField()
    endorser_date = models.DateField()

    def __str__(self):
        return f"Endorsement by {self.endorser_name}"
