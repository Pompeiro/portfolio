import factory
import factory.fuzzy
from django.core.files.base import ContentFile

from ..models import NEEDLE_CHOICES, UploadedImage


class UploadedImageFactory(factory.django.DjangoModelFactory):
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 1024, "height": 768}),
            "example.jpg",
        )
    )
    needle = factory.fuzzy.FuzzyChoice([x[0] for x in NEEDLE_CHOICES])
    threshold = factory.fuzzy.FuzzyFloat(0.0, 1.0)

    class Meta:
        model = UploadedImage
