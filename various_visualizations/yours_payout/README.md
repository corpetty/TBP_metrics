**Payout Model for Yours Network**

There are two functions that generate the data to be plot using the matplotlib and plotly package.  The first, 
a simple model, is based on a uniform distribution, and can be called using the `get_payouts_uniform` routine.  
It can be described as follows

Inputs:
- `max_tip`: Maximum tip given
- `num_tips`: number of tips
- `curator_payout_perc`: Percentage of tips paid out to curators
- `yours_payout_perc`: Percentage of tips paid to the Yours Network

Outputs a pandas DataFrame containing the following fields:
- `tip`: Initial tip given by currator
- `curator_payouts`: Payouts recieved from subsequent curator's tips
- `yours_revenue`: Amount of tip that is sent to Yours as revenue
- `curator_num`: curator number
- `total_earned`: cumulative amount earned by curator

The following is also printed to screen when executing the `get_payouts` routine:
- Total tipped
- Yours revenue
- Creator revenue
- Curator revenue

The second routine, a more advanced and realistic model, is based on a mixture of normal distributions.  
This model separates the curators into two groups:  A large group of small tippers, and a small group of large tippers.
This routine is named `get_payouts_mix_normal`.

Inputs:
- `tip_amounts`: list of tip amounts.  The last value will be the "high tipper" value.
- `num_tips`: number of tips
- `curator_payout_perc`: Percentage of tips paid out to curators
- `yours_payout_perc`: Percentage of tips paid to the Yours Network

The normal distributions are more sharply peaked around the "small tipper" amounts (sigma of 0.1) and make up 90% of
`num_tips`.  The remaining 10% of `num_tips`, is centered around the "high tipper" amount, and is broadly peaked 
(sigma of 0.8).

Everything else is the same as `get_payouts_uniform`. 

Package Requirements
- pandas
- numpy
- plotly
- matplotlip
- jupyter

Installing these can be done using the following command:

`> pip install <package_name>`

You can start the IPython notebook by entering:

`> jupyter CreateBubblePlot.ipynb ` or `> jupyter notebook` and selecting the correct notebook. 

Instructions for getting started with Plotly can be found [here](https://plot.ly/python/getting-started/)

More info on Jupyter notebooks can be found [here](https://jupyter-notebook-beginner-guide.readthedocs.org/en/latest/)

A quick tutorial on pandas can be found [here](http://pandas.pydata.org/pandas-docs/stable/10min.html)
