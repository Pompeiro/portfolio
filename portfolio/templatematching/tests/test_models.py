import pytest

pytestmark = pytest.mark.django_db


def test___str__(uploaded_image):
    assert uploaded_image.__str__() == str(uploaded_image.id)
    assert str(uploaded_image) == str(uploaded_image.id)


def test_get_absolute_url(uploaded_image):
    url = uploaded_image.get_absolute_url()

    assert url == f"/templatematching/{uploaded_image.slug}/"
