import pandas as pd
base_address = "F:\Pycharm"
hair_salon_df = pd.read_csv(base_address+ "\Hair-Salon-Establishment\dataset\hair_salon_no_show_wrangled_df.csv")
# print(hair_salon_df.head())
print(hair_salon_df.shape)
hair_salon_df.dropna(inplace=True)
# print(hair_salon_df.isna().sum())
columns_to_be_dropped = ["book_tod", "book_dow", "last_dow", "last_tod", "Unnamed: 0"]
for column in columns_to_be_dropped:
    # print(column)
    hair_salon_df.drop(column, axis=1, inplace=True)

# hair_salon_df.drop(hair_salon_df.index[[0]], inplace=True)
print(hair_salon_df.head())
hair_salon_df.to_csv(base_address+"\Hair-Salon-Establishment\dataset\hair_salon_munged.csv", index=False)
