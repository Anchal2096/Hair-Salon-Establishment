import pandas as pd

base_address = "F:\Pycharm"
hair_salon_df = pd.read_csv(base_address + "\Hair-Salon-Establishment\dataset\hair_salon_no_show_wrangled_df.csv")

print(hair_salon_df.shape)
hair_salon_df.dropna(inplace=True)
# print(hair_salon_df.isna().sum())
"""columns_to_be_dropped = ["book_tod", "book_dow", "last_dow", "last_tod", "Unnamed: 0", "last_receipt_tot"]
for column in columns_to_be_dropped:
    hair_salon_df.drop(column, axis=1, inplace=True)"""

# hair_salon_df.drop(hair_salon_df.index[[0]], inplace=True)
hair_salon_df.to_csv(base_address + "\Hair-Salon-Establishment\dataset\hair_salon_munged.csv", index=False)

""" assigning 0 to morning 1 to afternoon and 2 to evening """
for questions in range(1):
    for index, row in hair_salon_df.iterrows():
        print(row[1])
        if(row[1]) == "morning":
            row[1] = "0"
        elif (row[1]) == "afternoon":
            row[1] = "1"
        elif(row[1]) == "evening":
            row[1] = "2"
print(hair_salon_df["book_tod"])

