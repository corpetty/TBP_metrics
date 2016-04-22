**Payout Model for Yours Network**

The `get_payouts` function generates the data to be plot using the matplotlib and plotly package

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

Package Requirements
- pandas
- numpy
- plotly
- matplotlip
- jupyter

Installing these can be done using the following command:

`> pip install \<package_name>`

You can start the IPython notebook by entering:

`> jupyter CreateBubblePlot.ipynb ` or `> jupyter notebook` and selecting the correct notebook. 

Instructions for getting started with Plotly can be found [here](https://plot.ly/python/getting-started/)

More info on Jupyter notebooks can be found [here](https://jupyter-notebook-beginner-guide.readthedocs.org/en/latest/)
