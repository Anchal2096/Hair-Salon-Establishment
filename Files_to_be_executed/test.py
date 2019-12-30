import pandas as pd
from sklearn import preprocessing
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

""" assigning 2 to morning 0 to afternoon and 1 to evening """
# creating labelEncoder for normalising the label
le = preprocessing.LabelEncoder()
book_tod_encoded = le.fit_transform(hair_salon_df["book_tod"])
# print(" ENCODED : ", book_tod_encoded)
hair_salon_df["book_tod_encoded"] = book_tod_encoded
hair_salon_df.drop("book_tod", axis=1, inplace=True)
hair_salon_df.to_csv(base_address + "\Hair-Salon-Establishment\dataset\hair_salon_munged.csv", index=False)
# print(hair_salon_df["book_tod"])

