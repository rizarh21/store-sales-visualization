import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Store_ID': [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Store_Area': ['Bengawan', 'Jawa', 'Cidadap', 'Punclut', 'Dago_Giri', 'Bengawan_2', 'Babakan_Sari', 'Sukabumi',
                   'Kebon_Waru', 'Sukajadi', 'Cemara', 'Kebon_Bibit', 'Sersan_Sodik', 'Cipaku', 'Gegerkalong', 'Sarijadi',
                  'Setrasari','Babakan_Jeruk', 'Ambon', 'Ambon_2','Margahayu', 'Ciwaruga', 'Hegarmanah', 'Cigadung',
                   'Cikutra', 'Pahlawan', 'Suci', 'Cibadak', 'Lengkong', 'Inhoftank'],
    'Daily_Customer_Count': [510, 775, 470, 380, 420, 535, 690, 205, 240, 630, 330, 225, 210, 345, 570, 525, 465, 520, 665,
                             670, 885, 710, 560, 655, 730, 650, 885, 965, 1015, 652],
    'Item_Available': [1892, 2235, 1567, 1461, 1672, 1190, 1377, 1496, 1728, 1715, 1833, 1468, 1931, 2076, 1659, 1723, 1335,
                        1541, 1781, 1556, 1497, 1936, 2003, 1669, 1647, 1584, 1506, 1709, 1713, 1480],
    'Total_Sales_Per_Today': [6632085, 3587455, 4977020, 3322560, 5573500, 4662055, 6639085, 7021055, 5401080, 4785095,
                                    4106020, 5232030, 5765510, 4534050, 4901025, 5087550, 4985080, 6683530, 5572050, 7209540,
                                    3976030, 4065510, 5430550, 6755030, 6208500, 4339505, 5238090, 5671000, 4457540, 5587050]
}

df = pd.DataFrame(data)

highest_sales = df['Total_Sales_Per_Today'].max()
lowest_sales = df['Total_Sales_Per_Today'].min()

print("Highest selling branch:", highest_sales)
print("Lowest selling branch:", lowest_sales)

df['Target'] = df['Total_Sales_Per_Today'] >= 4000000

colors = []
max_index = df['Total_Sales_Per_Today'].idxmax()
min_index = df['Total_Sales_Per_Today'].idxmin()

for i in range (len(df)):
    if i == max_index:
        colors.append('green')
    elif i == min_index:
        colors.append('red')
    else:
        colors.append('skyblue')

plt.bar(df['Store_ID'], df['Total_Sales_Per_Today'], color=colors)
plt.title('Sales Per Branch (Green = Highest, Red = Lowest)')
plt.xlabel('Branch')
plt.ylabel('Sales')
plt.axhline(4000000, color='black', linestyle='--', label='Target Limit')
plt.legend()
plt.tight_layout()

plt.show()

df.to_csv('sales_data', index=False)