import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher['cnt']=teacher.groupby(['teacher_id'])['subject_id'].transform(lambda x:x.nunique())
    return teacher[['teacher_id','cnt']].drop_duplicates()
    