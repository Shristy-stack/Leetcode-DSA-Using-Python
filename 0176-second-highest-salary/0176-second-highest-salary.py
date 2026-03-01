import pandas as pd
import numpy as np
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['rank']=employee['salary'].rank(method='dense',ascending=False)
    p=employee.loc[employee['rank']==2,'salary'].drop_duplicates()
    if len(p)==0:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    else:
        return pd.DataFrame({'SecondHighestSalary':[p.iloc[0]]})

    

