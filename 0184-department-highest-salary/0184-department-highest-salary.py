import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(employee,department, left_on='departmentId',right_on='id')
    df=df.drop(["id_x","id_y","departmentId"],axis=1).rename(columns={"name_x":"Employee","name_y":"Department"})
    df["max_salary_dept"]=df.groupby("Department")['salary'].transform("max")
    df=df[df["salary"]==df["max_salary_dept"]]
    return df[['Department','Employee','salary']]