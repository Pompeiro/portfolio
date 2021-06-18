import pytest

from ..models import PortfolioProject

pytestmark = pytest.mark.django_db


def test___str__():
    project = PortfolioProject.objects.create(
        title="Mega super usefull project that will shine in my portfolio",
        description="The best project ever seen. You couldn't even imagine someone would invent this.",
        website="https://www.github.com/",
    )
    assert (
        project.__str__()
        == "Mega super usefull project that will shine in my portfolio"
    )
    assert str(project) == "Mega super usefull project that will shine in my portfolio"
