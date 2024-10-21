import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import chardet

filepath = os.path.expanduser("~/python-dataScience/superstoreProject/Sample-Superstore.csv")


#Checking encoding of my data.
with open(filepath, 'rb') as f:
    result = chardet.detect(f.read())
    print(result)


store_data = pd.read_csv(filepath,encoding='Windows-1252')
print(store_data.head(10))
print(store_data.info())

#Checking for duplicates in the data.

if store_data.duplicated().sum() > 1:
    print("There are duplicates in this data.")

else:
    print("There are no duplicates in this data.")

#Type of customers being served
type_of_customers = store_data["Segment"].unique()

print(type_of_customers)

#Number of customers being served per segment

number_of_customers = store_data["Segment"].value_counts().reset_index()
number_of_customers = number_of_customers.rename(columns={'Segment':'Type of customers'})
print(number_of_customers)

#Plotting the Number of customers
plt.figure(figsize=(10,8))
plt.title(" % of customers served (Per segment)")
plt.pie(number_of_customers['count'], labels=number_of_customers['Type of customers'],autopct='%1.1f%%')
plt.legend()
plt.savefig('visualizations/Number-of-customers.png')  # Save the figure as a PNG file
plt.close()

#Sales made per segment.
sales_per_segment = store_data.groupby("Segment")["Sales"].sum().reset_index()
sales_per_segment = sales_per_segment.rename(columns={"Segment":"Type of customer","Sales":"Total sales"})
print(sales_per_segment)
plt.bar(sales_per_segment["Type of customer"], sales_per_segment["Total sales"])
plt.savefig('visualizations/Sales-per-Segment.png')  # Save the figure as a PNG file
plt.close()

#Customer ordering frequency.
customer_frequency = store_data.groupby(["Customer ID","Customer Name","Segment"])["Order ID"].count().reset_index()
customer_frequency.rename(columns={"Order ID":"Total orders"},inplace=True)
repeat_customers = customer_frequency[customer_frequency["Total orders"] >= 1]
repeat_customers_sorted = repeat_customers.sort_values(by="Total orders",ascending=False)
print(repeat_customers.head(10).reset_index(drop=True))

#Customer sales.
customer_sales = store_data.groupby(["Customer ID","Customer Name","Segment"])["Sales"].sum().reset_index()
top_spenders =  customer_sales.sort_values(by="Sales",ascending=False)
print(top_spenders.head(10))

#Shipping model.
shipping_model = store_data["Ship Mode"].value_counts().reset_index()
shipping_model = shipping_model.rename(columns={"Index":"Use frequency","Ship Mode":"Mode of shipment"})
print(shipping_model)

plt.figure(figsize=(10,8))
plt.title(" % of shipping modes used")
plt.pie(shipping_model["count"], labels=shipping_model["Mode of shipment"],autopct='%1.1f%%')
plt.savefig('visualizations/modes-of-shipment.png')  # Save the figure as a PNG file
plt.close()

#Number of Customers per state...
state = store_data["State"].value_counts().reset_index()
state = state.rename(columns={"State":"Number of customers"})
print(state.head(10))

#Number of customers per city.
city = store_data["City"].value_counts().reset_index()
print(city.head(10))

#Calculating State top sales

state_sales = store_data.groupby("State")["Sales"].sum().reset_index()
top_sales = state_sales.sort_values(by="Sales",ascending=False)
print(round(top_sales.head(10).reset_index(drop=True),2))

#Calculating City top sales
city_sales = store_data.groupby("City")["Sales"].sum().reset_index()
top_city_sales = city_sales.sort_values(by="Sales",ascending=False)
print(round(top_city_sales.head(10).reset_index(drop=True),2))

#product sub-category analysis
product_subcategory = store_data["Sub-Category"].unique()
print(product_subcategory)

#Sub-Category counts
subcategory_count = store_data.groupby('Category')['Sub-Category'].nunique().reset_index()
subcategory_count = subcategory_count.sort_values(by='Sub-Category', ascending = False)
print(subcategory_count)

#Category sales
category_sales = store_data.groupby("Category")["Sales"].sum().reset_index()
category_sales = category_sales.sort_values(by="Sales",ascending=False)
print(category_sales.reset_index(drop=True))
plt.pie(category_sales['Sales'], labels=category_sales['Category'], autopct='%1.1f%%')
plt.legend()
plt.savefig('visualizations/sales-per-category.png')  # Save the figure as a PNG file
plt.close()

#Sub category sales

subcategory_sales = store_data.groupby(["Category","Sub-Category"])["Sales"].sum().reset_index()
subcategory_sales = subcategory_sales.sort_values(by="Sales",ascending=False)
print(subcategory_sales.reset_index(drop=True))
subcategory_sales = subcategory_sales.sort_values(by="Sales",ascending=True)

plt.figure(figsize=(10,8))
plt.title("Sub-category sales")
plt.xlabel("Sales in $")
plt.ylabel("Sub Category")
plt.barh(subcategory_sales["Sub-Category"],subcategory_sales["Sales"],color=plt.cm.plasma(np.linspace(0, 1, len(subcategory_sales["Sales"]))))
plt.savefig('visualizations/sub-category-sales.png')  # Save the figure as a PNG file
plt.close()


#Analysing the yearly sales
store_data['Order Date'] = pd.to_datetime(store_data['Order Date'],errors='coerce')
yearly_sales = store_data.groupby(store_data['Order Date'].dt.year)['Sales'].sum()
yearly_sales = yearly_sales.reset_index()
yearly_sales = yearly_sales.rename(columns={'Order Date' : 'Year', 'Sales': 'Total Sales'})

print (yearly_sales)
plt.bar(yearly_sales["Year"],yearly_sales["Total Sales"])
plt.plot(yearly_sales["Year"],yearly_sales["Total Sales"],marker = 'o',linestyle='-')
plt.savefig('visualizations/yearly-sales.png')  # Save the figure as a PNG file
plt.close()


#Let's analyse the monthly say for the year lets say 2020.
store_data["Order Date"] = pd.to_datetime(store_data["Order Date"],errors='coerce')
year_sales = store_data[store_data["Order Date"].dt.year == 2017]
year_sales.set_index("Order Date", inplace=True)
quartely_sales = year_sales.resample("Q")["Sales"].sum() 
quartely_sales = quartely_sales.reset_index()
quartely_sales = quartely_sales.rename(columns={"Order Date":"Quarter","Sales":"Total sales"})
print(quartely_sales)
plt.figure(figsize=(12,10))
plt.plot(quartely_sales["Quarter"],quartely_sales["Total sales"])
plt.savefig('visualizations/quarterly-sales.png')  # Save the figure as a PNG file
plt.close()

