import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(customers,orders, how="left", left_on="id",right_on="customerId")
    df=df[df['customerId'].isnull()].drop(['id_x','id_y','customerId'],axis=1)
    df=df.rename(columns={'name':'Customers'})
    return df