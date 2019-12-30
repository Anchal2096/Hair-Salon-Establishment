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
hair_salon_df["book_tod_encoded"] = book_tod_encoded
hair_salon_df.drop("book_tod", axis=1, inplace=True)

book_dow_encoded = le.fit_transform(hair_salon_df["book_dow"])
hair_salon_df["book_dow_encoded"] = book_dow_encoded
hair_salon_df.drop("book_dow", axis=1, inplace=True)


book_category_encoded = le.fit_transform(hair_salon_df["book_category"])
hair_salon_df["book_category_encoded"] = book_category_encoded
hair_salon_df.drop("book_category", axis=1, inplace=True)


book_staff_encoded = le.fit_transform(hair_salon_df["book_staff"])
hair_salon_df["book_staff_encoded"] = book_staff_encoded
hair_salon_df.drop("book_staff", axis=1, inplace=True)


last_category_encoded = le.fit_transform(hair_salon_df["last_category"])
hair_salon_df["last_category_encoded"] = last_category_encoded
hair_salon_df.drop("last_category", axis=1, inplace=True)


last_staff_encoded = le.fit_transform(hair_salon_df["last_staff"])
hair_salon_df["last_staff_encoded"] = last_staff_encoded
hair_salon_df.drop("last_staff", axis=1, inplace=True)


last_receipt_tot_encoded = le.fit_transform(hair_salon_df["last_receipt_tot"])
hair_salon_df["last_receipt_tot_encoded"] = last_receipt_tot_encoded
hair_salon_df.drop("last_receipt_tot", axis=1, inplace=True)


last_dow_encoded = le.fit_transform(hair_salon_df["last_dow"])
hair_salon_df["last_dow_encoded"] = last_dow_encoded
hair_salon_df.drop("last_dow", axis=1, inplace=True)


last_tod_encoded = le.fit_transform(hair_salon_df["last_tod"])
hair_salon_df["last_tod_encoded"] = last_tod_encoded
hair_salon_df.drop("last_tod", axis=1, inplace=True)


hair_salon_df.to_csv(base_address + "\Hair-Salon-Establishment\dataset\hair_salon_munged.csv", index=False)
# print(hair_salon_df["book_tod"])

