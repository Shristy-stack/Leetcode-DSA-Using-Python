import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    #df=employee[employee['id'].isin(employee['managerId'])]
    employee['cnt']=employee.groupby('managerId')['id'].transform('count')
    p=employee[employee['cnt']>=5]
    q=p['managerId'].drop_duplicates()
    r=employee[employee['id'].isin(q)][['name']]
    return r