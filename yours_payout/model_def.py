__author__ = 'Corey Petty'
import pandas as pd
import numpy as np


def get_payouts(max_tip, num_tips, curator_payout_perc, yours_payout_perc) -> pd.DataFrame:
    tips = np.random.uniform(0.00001, max_tip, num_tips)
    curator_payouts = [list() for _ in range(num_tips)]
    yours_payouts = []
    for current_tipper, current_tip in enumerate(tips, 1):
        current_total = sum(tips[:current_tipper])
        current_tip_perc = current_tip / current_total
        for payer_num in range(0, current_tipper):
            curator_payouts[payer_num].append(tips[payer_num] * curator_payout_perc * current_tip_perc)
        yours_payouts.append(yours_payout_perc*current_tip)
    df = pd.DataFrame([tips, curator_payouts, yours_payouts])
    df = df.transpose()
    df.columns = ['tip', 'curator_payouts', 'yours_revenue']
    df['curator_num'] = [x for x in range(num_tips)]
    df['total_earned'] = [sum(x) for x in df.curator_payouts]

    # Print some stats to screen
    print('Total tipped:    ${0:.2f}'.format(round(df.tip.sum(), 2)))
    print('Yours revenue:   ${0:.2f}'.format(round(df.yours_revenue.sum(), 2)))
    print('Creator revenue: ${0:.2f}'.format(round(df.tip.sum() * (1 - (yours_payout_perc + curator_payout_perc)), 2)))
    print('Curator revenue: ${0:.2f}'.format(round(df.total_earned.sum(), 2)))
    return df
