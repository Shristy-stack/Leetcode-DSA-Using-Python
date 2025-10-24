import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders['count']=orders.groupby('customer_number')['order_number'].transform('count')
    maxp=orders['count'].max()
    res=orders.loc[orders['count']==maxp]
    return res[['customer_number']].drop_duplicates()
