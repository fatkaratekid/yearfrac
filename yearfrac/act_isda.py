
from .isaleapyear import isaleapyear
from .julianday import date_to_jd


def act_isda(y1, m1, d1, y2, m2, d2):

    if y1 is y2:
        diff_days = date_to_jd(y2, m2, d2) - date_to_jd(y1, m1, d1)
        denom = 366e0 if isaleapyear(y2) else 365e0

        if diff_days < 0:
            raise Exception(
                "Newer date y2-m2-d2 is older than previous date y1-m1-d1.")
        elif diff_days is 0:
            return 0e0
        else:
            return diff_days / denom

    elif y1 < y2:
        diffa = date_to_jd(y1, 12, 31) - date_to_jd(y1, m1, d1)
        denoma = 366e0 if isaleapyear(y1) else 365e0

        diffb = date_to_jd(y2, m2, d2) - date_to_jd(y2, 1, 1)
        denomb = 366e0 if isaleapyear(y2) else 365e0

        diffy = (y2 - y1 - 1)
        return (diffa / denoma) + (diffb / denomb) + diffy

    else:
        raise Exception(
            "Newer date y2-m2-d2 is older than previous date y1-m1-d1.")
