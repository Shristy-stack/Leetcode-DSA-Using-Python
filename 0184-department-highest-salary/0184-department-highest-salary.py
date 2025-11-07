import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(employee,department, left_on='departmentId',right_on='id')
    df=df.drop(columns={'id_x','id_y'}).rename(columns={'name_x':'Employee','name_y':'Department','salary':'Salary'})
    df['max_salary']=df.groupby('Department')['Salary'].transform('max')
    df=df.loc[df['Salary']==df['max_salary']]
    return df[['Department','Employee','Salary']]