import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(employee,department,left_on='departmentId',right_on='id')
    df['Salary']=df.groupby('departmentId')['salary'].transform('max')
    p=df[df['salary']==df['Salary']]
    return p[['name_y','name_x','Salary']].rename(columns={'name_y':'Department','name_x':'Employee'})