def generate_id(df):
    return f"S{len(df)+1:03d}"

def calculate_average_grade(row):
    avg = (row["Math"] + row["Science"] + row["English"]) / 3
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "F"
    return round(avg, 2), grade

import pandas as pd

def add_student(df, name, cls, math, sci, eng):
    sid = generate_id(df)
    avg, grade = calculate_average_grade({"Math": math, "Science": sci, "English": eng})
    new_row = pd.DataFrame([{
        "Student ID": sid, "Name": name, "Class": cls,
        "Math": math, "Science": sci, "English": eng,
        "Average": avg, "Grade": grade
    }])
    return pd.concat([df, new_row], ignore_index=True)


def update_marks(df, sid, math, sci, eng):
    idx = df[df["Student ID"] == sid].index
    if not idx.empty:
        i = idx[0]
        df.loc[i, ["Math", "Science", "English"]] = [math, sci, eng]
        avg, grade = calculate_average_grade(df.loc[i])
        df.loc[i, "Average"] = avg
        df.loc[i, "Grade"] = grade
    return df
