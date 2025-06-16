def class_wise_average(df):
    return df.groupby("Class")[["Math", "Science", "English", "Average"]].mean()

def subject_topper(df, subject):
    return df.loc[df[subject].idxmax()]
