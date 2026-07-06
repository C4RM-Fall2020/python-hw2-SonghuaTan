import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):

    t = np.arange(1, m * ppy + 1)

    coupon = face * couponRate / ppy

    cashflow = np.full(m * ppy, coupon)
    cashflow[-1] += face

    pv = 1 / (1 + y / ppy) ** t

    pvcf = cashflow * pv

    duration = np.sum((t / ppy) * pvcf) / np.sum(pvcf)

    return duration
