import pandas as pd

data = pd.read_csv("C:/Users/human/ku-python/data/HM_all_stores.csv")

data.info()

# tidy = data.melt(id_vars="storeCode", var_name="dataName", value_name="data")
# print(tidy)

print(data.columns)

tidy = data.melt(id_vars=['storeCode', 'storeClass', 'name', 'phone', 'city', 'country',
                        'countryCode', 'longitude', 'latitude', 'timeZoneIndex',], 
                    var_name="openingHours",
                    value_vars=['Mon_open_hours', 'Tue_open_hours', 'Wed_open_hours', 'Thu_open_hours',
                        'Fri_open_hours', 'Sat_open_hours', 'Sun_open_hours'],
                        value_name="day")

print(tidy)