import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_sorted_values=employee['salary'].dropna().drop_duplicates().sort_values(ascending= False)
    if len(unique_sorted_values)<2:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    else:
        return pd.DataFrame({'SecondHighestSalary':[unique_sorted_values.iloc[1]]})
    