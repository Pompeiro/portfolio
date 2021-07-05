import pathlib

import cv2 as cv
import numpy as np
from django.conf import settings


def get_matched_image(image, needle, threshold=0.95):
    if not needle:
        return image
    else:
        needle_path = pathlib.PurePath(
            settings.STATIC_ROOT
            + f"/images/templatematching/templatematching_needles/{needle}.jpg"
        )
        template_rgb = str(needle_path)
        img_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread(template_rgb, 0)
        w, h = template.shape[::-1]

        res = cv.matchTemplate(img_gray, template, cv.TM_CCORR_NORMED)
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        return cv.cvtColor(img_rgb, cv.COLOR_BGR2RGB)
