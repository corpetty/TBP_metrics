__author__ = 'Corey Petty'
import pandas as pd
import numpy as np
from datetime import timedelta


def get_payouts_uniform(max_tip, num_tips, curator_payout_perc, yours_payout_perc) -> pd.DataFrame:
    tips = np.random.uniform(0.00001, max_tip, num_tips)
    curator_payouts = [list() for _ in range(0, num_tips)]
    yours_payouts = tips * yours_payout_perc
    for current_tipper, current_tip in enumerate(tips, 1):
        distribution_total = sum(tips[:current_tipper-1])
        for payout_num in range(0, current_tipper-1):
            payout_tip_perc = tips[payout_num] / distribution_total
            curator_payouts[payout_num].append(current_tip * curator_payout_perc * payout_tip_perc)

    df = pd.DataFrame([tips, curator_payouts, yours_payouts])
    df = df.transpose()
    df.columns = ['tip', 'curator_payouts', 'yours_revenue']
    df['curator_num'] = [x for x in range(num_tips)]
    df['total_earned'] = [sum(x) for x in df.curator_payouts]

    # Print some stats to screen
    print('Total tipped:    ${0:.2f}'.format(round(df.tip.sum(), 2)))
    print('Yours revenue:   ${0:.2f}'.format(round(df.yours_revenue.sum(), 2)))
    print('Creator revenue: ${0:.2f}'.format(round(df.tip[1:].sum() * (1 - (yours_payout_perc + curator_payout_perc))
                                                   + df.tip[0] * (1 - yours_payout_perc), 2)))
    print('Curator revenue: ${0:.2f}'.format(round(df.total_earned.sum(), 2)))
    return df


def get_payouts_mixed_normal(tip_amounts, num_tips, curator_payout_perc, yours_payout_perc) -> pd.DataFrame:
    # Create mixed set of normal distributions, centered around each tip amount provided
    #   in tip_amounts.
    #   Assumed that last tip amount is an outlier, will be 10% of num_tips,
    #   and be more spread out than other distributions
    sigmas = [0.1 for _ in range(len(tip_amounts))]
    sigmas[-1] = 0.8                # spread out outlier tips
    sizes = [(0.9 * num_tips) / (len(tip_amounts) - 1) for _ in range(len(tip_amounts))]
    sizes[-1] = 0.1 * num_tips
    distributions = [np.random.normal(mu, sigma, int(size)) for mu, sigma, size in zip(tip_amounts, sigmas, sizes)]
    tips = np.concatenate(distributions)
    # Randomize the tips
    np.random.shuffle(tips)

    curator_payouts = [list() for _ in range(0, num_tips)]
    yours_payouts = tips * yours_payout_perc
    for current_tipper, current_tip in enumerate(tips, 1):
        distribution_total = sum(tips[:current_tipper-1])
        for payout_num in range(0, current_tipper-1):
            payout_tip_perc = tips[payout_num] / distribution_total
            curator_payouts[payout_num].append(current_tip * curator_payout_perc * payout_tip_perc)

    df = pd.DataFrame([tips, curator_payouts, yours_payouts])
    df = df.transpose()
    df.columns = ['tip', 'curator_payouts', 'yours_revenue']
    df['curator_num'] = [x for x in range(num_tips)]
    df['total_earned'] = [sum(x) for x in df.curator_payouts]

    # Print some stats to screen
    print('Total tipped:    ${0:.2f}'.format(round(df.tip.sum(), 2)))
    print('Yours revenue:   ${0:.2f}'.format(round(df.yours_revenue.sum(), 2)))
    print('Creator revenue: ${0:.2f}'.format(round(df.tip[1:].sum() * (1 - (yours_payout_perc + curator_payout_perc))
                                                   + df.tip[0] * (1 - yours_payout_perc), 2)))
    print('Curator revenue: ${0:.2f}'.format(round(df.total_earned.sum(), 2)))
    return df


def get_payouts_mixed_normal_with_time(tip_amounts, tip_timings, num_tips, curator_payout_perc, yours_payout_perc) -> pd.DataFrame:
    # Create mixed set of normal distributions, centered around each tip amount provided
    #   in tip_amounts.
    #   Assumed that last tip amount is an outlier, will be 10% of num_tips,
    #   and be more spread out than other distributions
    # The same procedure is done with the timings of tips
    sigmas = [0.1 for _ in range(len(tip_amounts))]
    sigmas[-1] = 0.8  # spread out outlier tips
    sizes = [(0.9 * num_tips) / (len(tip_amounts) - 1) for _ in range(len(tip_amounts))]
    sizes[-1] = 0.1 * num_tips
    tip_distributions = [np.random.normal(mu, sigma, int(size)) for mu, sigma, size in zip(tip_amounts, sigmas, sizes)]
    time_distributions = [np.random.normal(mu, sigma, int(size)) for mu, sigma, size in zip(tip_timings, sigmas, sizes)]
    tips = np.concatenate(zip(tip_distributions, time_distributions))
    # Randomize the tips
    np.random.shuffle(tips)

    curator_payouts = [list() for _ in range(0, num_tips)]
    yours_payouts = tips * yours_payout_perc
    channel_open_num = 0
    for current_tipper, (current_tip, current_time) in enumerate(tips, 1):
        distribution_total = sum(tips[channel_open_num:current_tipper - 1])
        for payout_num in range(0, current_tipper - 1):

            if channel_lifetime <= timedelta(days=1):
                payout_tip_perc = tips[payout_num] / distribution_total
                curator_payouts[payout_num].append(current_tip * curator_payout_perc * payout_tip_perc)
            else:
                channel_close_num = payout_num

    df = pd.DataFrame([tips, curator_payouts, yours_payouts])
    df = df.transpose()
    df.columns = ['tip', 'curator_payouts', 'yours_revenue']
    df['curator_num'] = [x for x in range(num_tips)]
    df['total_earned'] = [sum(x) for x in df.curator_payouts]

    # Print some stats to screen
    print('Total tipped:    ${0:.2f}'.format(round(df.tip.sum(), 2)))
    print('Yours revenue:   ${0:.2f}'.format(round(df.yours_revenue.sum(), 2)))
    print('Creator revenue: ${0:.2f}'.format(round(df.tip[1:].sum() * (1 - (yours_payout_perc + curator_payout_perc))
                                                   + df.tip[0] * (1 - yours_payout_perc), 2)))
    print('Curator revenue: ${0:.2f}'.format(round(df.total_earned.sum(), 2)))
    return df