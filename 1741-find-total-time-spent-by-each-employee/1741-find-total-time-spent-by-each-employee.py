import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['diff']=employees['out_time']-employees['in_time']
    employees['total_time']=employees.groupby(['emp_id','event_day'])['diff'].transform('sum')
    return employees[['event_day','emp_id','total_time']].drop_duplicates().rename(columns={'event_day':'day'})
    
    