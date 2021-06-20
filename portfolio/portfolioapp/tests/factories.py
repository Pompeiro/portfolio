import factory
import factory.fuzzy
from django.template.defaultfilters import slugify

from ..models import PortfolioProject

# https://stackoverflow.com/questions/36452363/how-to-use-py-test-fixtures-without-importing-them
# https://stackoverflow.com/questions/46089480/pytest-fixtures-redefining-name-from-outer-scope-pylint


class PortfolioProjectFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    description = factory.Faker("paragraph", nb_sentences=5, variable_nb_sentences=True)
    website = factory.Faker("url")
    photo = factory.Faker("image_url")

    class Meta:
        model = PortfolioProject
