import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities_count=activities.groupby('sell_date').agg(
        num_sold=('product', lambda x: x.nunique()),
        products=('product', lambda x: ','.join(sorted(x.unique())))
    ).reset_index().sort_values('sell_date')
    return activities_count