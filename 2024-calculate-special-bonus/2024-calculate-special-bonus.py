import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition=employees['bonus']=(employees['employee_id']%2!=0) & (~employees['name'].str.startswith("M"))
    employees['bonus']=0
    employees.loc[condition,'bonus']=employees['salary']
    return employees[['employee_id','bonus']].sort_values('employee_id')
    