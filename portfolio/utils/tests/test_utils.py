import pathlib

import cv2 as cv
import numpy as np
import pytest
from django.conf import settings

from ..utils import get_matched_image

pytestmark = pytest.mark.django_db


def test_get_matched_image_with_needle_none(photo):
    result = get_matched_image(image=photo, needle=None)
    assert photo == result


def test_get_matched_image_with_needle():
    img_path = pathlib.PurePath(
        settings.STATIC_ROOT
        + "/images/templatematching/templatematching_needles/acceptGameButton.jpg"
    )
    img_rgb = str(img_path)
    img_rgb = cv.imread(img_rgb)
    result = get_matched_image(image=img_rgb, needle="acceptGameButton", threshold=0.95)

    # success in template matching result in marking image with rectangle
    assert np.sum(img_rgb) != np.sum(result)


def test_get_matched_image_with_needle_where_result_is_not_found():
    img_path = pathlib.PurePath(
        settings.STATIC_ROOT
        + "/images/templatematching/templatematching_needles/findMatchButton.jpg"
    )
    img_rgb = str(img_path)
    img_rgb = cv.imread(img_rgb)
    result = get_matched_image(
        image=img_rgb, needle="confirmationButton", threshold=0.99
    )

    # fail in template matching result in NOT marking image with rectangle
    assert np.sum(img_rgb) == np.sum(result)
