import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\sadhana s\\student_data.csv")
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',None)
#display all data
print(df)
print(df.describe())
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull().sum())
# Drop unnamed column
df=df.drop("Height",axis=1)
print(df.head())

# Get the column names
columns_to_find = ['Maths', 'Science', 'English', 'Kannada', 'Social Science', 'Hindi']
existing_columns = {}

for column in columns_to_find:
    matching_columns = [col for col in df.columns if column.lower() in col.lower()]
    if matching_columns:
        existing_columns[column] = matching_columns[0]
    else:
        print(f"Column '{column}' not found.")

# Calculate the total marks
total_marks_columns = [existing_columns[col] for col in existing_columns]
df['Total Marks'] = df[total_marks_columns].sum(axis=1)

# Print the column names
print(df.columns)

# Display the 'Total Marks' column
print(df['Total Marks'])
#Calculate the average for Total marks
average=(df['Total Marks']/6)
#display the 'average'column
print(average)
#create a gender plot
plt.figure(figsize=(4,5))
ax=sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
plt.show()
print(df["Pratice Sport"].unique())
R=df.loc[(df['Pratice Sport']=="R")].count()
N=df.loc[(df['Pratice Sport']=="N")].count()
S=df.loc[(df['Pratice Sport']=="S")].count()
l=["R","N","S"]
colors=['red','blue','green']
mlist=[R["Pratice Sport"],N["Pratice Sport"],S["Pratice Sport"]]
plt.pie(mlist,labels=l,autopct= "%1.2f%%",colors=colors)
plt.title('Pratice Sport')
plt.show()
Column=df['Weight']
print(Column)
sns.heatmap(Column.values.reshape(1,-1),annot=True,cmap='coolwarm',square=True)
plt.show()







