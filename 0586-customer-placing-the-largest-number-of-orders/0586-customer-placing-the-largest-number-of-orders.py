import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders['cnts']=orders.groupby('customer_number')['order_number'].transform('count')
    orders=orders.loc[orders['cnts']==orders['cnts'].max()]
    return orders[['customer_number']].drop_duplicates()