import pandas as pd

# Load the data
df = pd.read_csv('./datas/bids.csv')

# 1. Get the number of unique IPs per auction
auctionIpCounts = df.groupby('auction')['ip'].nunique().reset_index()
print(auctionIpCounts)