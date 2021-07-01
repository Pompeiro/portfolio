from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse


class PortfolioProject(models.Model):
    title = models.CharField("Title of project", max_length=100, unique=True)
    description = models.TextField("Description", blank=True)
    website = models.URLField(blank=True)
    try_online_url = models.URLField(blank=True)
    photo = models.ImageField(
        upload_to="portfolioapp", default="portfolioapp/blank_project.jpg"
    )
    slug = AutoSlugField(
        "Project address", unique=True, always_update=False, populate_from="title"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return absolute URL to the PortfolioProject Detail page."""
        return reverse("portfolioapp:detail", kwargs={"slug": self.slug})


class Technology(models.Model):
    technology = models.CharField(max_length=200)
    project = models.ForeignKey(
        PortfolioProject, on_delete=models.CASCADE, to_field="title"
    )

    def __str__(self):
        return self.technology
