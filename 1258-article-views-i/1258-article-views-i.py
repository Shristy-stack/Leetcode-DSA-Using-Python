import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df=views[views['author_id']==views['viewer_id']].drop_duplicates(subset=['author_id'])
    return df[['author_id']].sort_values(by='author_id').rename(columns={'author_id':'id'})
    