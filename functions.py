def kmh_to_ms(v):
    return v / 3.6


def ms_to_kmh(v):
    return v * 3.6


def compare(v1_ms, v2):
    if v1_ms > v2:
        return "v1 більше"
    elif v1_ms < v2:
        return "v2 більше"
    else:
        return "однакові"