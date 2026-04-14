def kmh_to_ms(v):
    return v / 3.6


def ms_to_kmh(v):
    return v * 3.6


# ---------- VARIANT 19 ----------
def compare_speed(v1, v2):
    v1_ms = kmh_to_ms(v1)
    if v1_ms > v2:
        return "v1 більше"
    elif v1_ms < v2:
        return "v2 більше"
    return "однакові"


# ---------- VARIANT 20 ----------
def convert_time(h, m):
    if h < 0 or h > 23 or m < 0 or m > 59:
        return None, "Incorrect time!"

    period = "am" if h < 12 else "pm"
    hour_12 = h % 12
    if hour_12 == 0:
        hour_12 = 12

    return f"{hour_12}:{m:02d} {period}", None


# ---------- VARIANT 21 ----------
def time_to_midnight(h, m, part):
    if h < 1 or h > 12 or m < 0 or m > 59:
        return None

    if part == "a":  # am
        total_minutes = (12 * 60) - (h % 12) * 60 - m
    else:  # pm
        total_minutes = (24 * 60) - (h % 12 + 12) * 60 - m

    hours = total_minutes // 60
    minutes = total_minutes % 60

    return hours, minutes