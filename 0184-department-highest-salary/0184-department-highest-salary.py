import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(employee,department,left_on='departmentId',right_on='id')
    dff=df.drop(columns=['id_y']).rename(columns={'id_x':'emp_id','name_x':'Employee','salary':'Salary','name_y':'Department'})
    dff['max_salary']=dff.groupby(['departmentId','Department'])['Salary'].transform('max')
    res=dff.loc[dff['Salary']==dff['max_salary']].drop(columns=['max_salary'])
    return res[['Department','Employee','Salary']]