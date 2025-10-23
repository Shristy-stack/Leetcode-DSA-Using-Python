import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    unique_leads=daily_sales.groupby(['date_id','make_name'])['lead_id'].nunique().reset_index()
    unique_leads.rename(columns={'lead_id':'unique_leads'},inplace = True)
    unique_partners=daily_sales.groupby(['date_id','make_name'])['partner_id'].nunique().reset_index()
    unique_partners.rename(columns={'partner_id':'unique_partners'},inplace = True)
    df=pd.merge(unique_leads,unique_partners, on=['date_id','make_name'])
    return df
    