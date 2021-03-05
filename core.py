import pandas as pd 
from collections import Counter
import psycopg2
from sqlalchemy import create_engine

# conn = psycopg2.connect(
#     host="localhost", database="cafe_data", user="postgres", password="docker"
# )

# mycursor = conn.cursor()

df = pd.read_csv('sales_data_new.csv')
df.dropna(inplace = True) 
df.drop(['x', 'name'], axis=1, inplace=True)

# alchemyEngine = create_engine("postgresql://postgres:docker@localhost:5432/cafe_data")

# # Connect to PostgreSQL server
# dbConnection = alchemyEngine.connect();
# postgreSQLConnection = alchemyEngine.connect();
# postgreSQLTable= "raw_transaction";

# try:
#     frame = df.to_sql(postgreSQLTable, postgreSQLConnection, if_exists='fail');
# except ValueError as vx:
#     print(vx)
# except Exception as ex:  
#     print(ex)
# else:
#     print("PostgreSQL Table %s has been created successfully."%postgreSQLTable);
# finally:
#     postgreSQLConnection.close();


# dropping null value columns to avoid errors 
df.dropna(inplace = True) 

df['order']=df['order'].str.split(",")
df['order']

# print(df['order'])

df1=[]

for i in range(df.shape[0]):
    for j in df['order'][i]:
        df1.append(j)
        


df_list=df['order']

list_1=list(set(df1))

list_2=[x.strip(' ') for x in list_1]

list_3=list(set(list_2))




products = []
for order in list_3:
    if order == "Large" or "." in order or "Regular" in order:
        pass
    else:
        products.append(order)

x=products.pop(0)
y=pd.factorize(products)
print(y)

number_of_elements = len(products)

print(number_of_elements)

# groupby_sum1 = df.groupby(['customer_id']).sum()

# list_string = df_list.str.cat(sep=',')

# list_string=list_string.split(',')

# list_split_all=[x.strip(' ') for x in list_split]

# count = Counter(list_split_all)

# unique_list = list(count.keys())
# print(unique_list)

# # Dropping old Name columns 
# df.drop(columns =["Name"], inplace = True) 





# split_data = df["order"].str.split(", ")
# data = split_data.to_list()
# names = ["size","product","price","size 2","size 5"]
# new_df = pd.DataFrame(data, columns=names)


# groupby_sum1 = df.groupby(['customer_id']).sum()

# groupby_sum2 = df.groupby(['customer_id']).mean()

# df3 = df.groupby(['customer_id','product_id']).size().reset_index(name='count')

# i = df[(df['purchase_date'] >= '2020-12-01') & (df['purchase_date'] <= '2020-12-05')]
# print(i)