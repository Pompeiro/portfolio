from autoslug import AutoSlugField
from django.db import models


class PortfolioProject(models.Model):
    title = models.CharField("Title of project", max_length=100)
    description = models.TextField("Description", blank=True)
    website = models.URLField(blank=True)
    photo = models.ImageField(
        upload_to="portfolioapp", default="portfolioapp/blank_project.jpg"
    )
    slug = AutoSlugField(
        "Project address", unique=True, always_update=False, populate_from="title"
    )

    def __str__(self):
        return self.title
