from io import BytesIO

import numpy as np
from autoslug import AutoSlugField
from django.core.files.base import ContentFile
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from PIL import Image

from ..utils.utils import get_matched_image

NEEDLE_CHOICES = (
    ("acceptGameButton", "Accept game button"),
    ("afterLogINButton", "After login button(play button)"),
    ("confirmationButton", "Confirmation button"),
    ("findMatchButton", "Find match button"),
    ("inQueueFindingMatch", "In queue finding match text"),
    ("playGameButton", "Play game button"),
)

THRESHOLD_LOWER_CONSTRAINT = 0.0
THRESHOLD_UPPER_CONSTRAINT = 1.0


class UploadedImage(TimeStampedModel):
    image = models.ImageField("Haystack image", upload_to="templatematching")
    needle = models.CharField(
        "Needle image", max_length=50, choices=NEEDLE_CHOICES, blank=True
    )
    threshold = models.FloatField("Match threshold, range:0.0-1.0", default=0.95)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(threshold__gte=THRESHOLD_LOWER_CONSTRAINT)
                & models.Q(threshold__lte=THRESHOLD_UPPER_CONSTRAINT),
                name="A dps value is valid between 0.0 and 1.0",
            )
        ]

    # https://stackoverflow.com/questions/4380879/django-model-field-default-based-off-another-field-in-same-model

    def populate_slug(self):
        return self.image.name.replace("templatematching/", "").replace(".jpg", "")

    slug = AutoSlugField(
        "Uploaded Image address",
        unique=True,
        always_update=False,
        populate_from=populate_slug,
    )

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        pil_img = Image.open(self.image)
        cv_img = np.array(pil_img)
        img = get_matched_image(cv_img, self.needle, self.threshold)
        im_pil = Image.fromarray(img)

        buffer = BytesIO()
        im_pil.save(buffer, format="JPEG")
        image_jpg = buffer.getvalue()
        self.image.save(str(self.image), ContentFile(image_jpg), save=False)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute URL to the champion Detail page."""
        return reverse("templatematching:detail", kwargs={"slug": self.slug})
