import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    filter_df=world[['name','population','area']]
    res=filter_df[(filter_df['population']>=25000000) | (filter_df['area']>=3000000)]
    return res