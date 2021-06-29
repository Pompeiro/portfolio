from io import BytesIO

import numpy as np
from django.core.files.base import ContentFile
from django.db import models
from model_utils.models import TimeStampedModel
from PIL import Image
from utils.utils import get_matched_image

NEEDLE_CHOICES = (
    ("acceptGameButton", "Accept game button"),
    ("afterLogINButton", "After login button(play button)"),
    ("confirmationButton", "Confirmation button"),
    ("findMatchButton", "Find match button"),
    ("inQueueFindingMatch", "In queue finding match text"),
    ("playGameButton", "Play game button"),
)


class UploadedImage(TimeStampedModel):
    image = models.ImageField(upload_to="templatematching")
    needle = models.CharField(max_length=50, choices=NEEDLE_CHOICES)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        pil_img = Image.open(self.image)
        cv_img = np.array(pil_img)
        img = get_matched_image(cv_img, self.needle)
        im_pil = Image.fromarray(img)

        buffer = BytesIO()
        im_pil.save(buffer, format="JPEG")
        image_jpg = buffer.getvalue()
        self.image.save(str(self.image), ContentFile(image_jpg), save=False)

        super().save(*args, **kwargs)
