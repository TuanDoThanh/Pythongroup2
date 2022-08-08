 # Read the file "OrdersandDeliveries.csv" to process the data.
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import os


# data = pd.read_csv('OrdersandDeliveries.csv')
# print(data.to_string())
# data.info()

# data.isnull().values.any()
# if data == True:
#     print("The data variable has None Value")
# else:
#     print("It does not have None value")

# data.isnull().sum().sum()
# data.isnull().sum()
# data.show()

# def clear_data(path, pattern)
#     data = getBufferData(path)
#     new_data = []

#     regex = re.compile('['+ pattern + ']')
#     #clear data
#     for i in range(0, len(data)):
#         new_data.append([])
#         for j in range(len(data[i])):
#             if j < 2:
#                 if data[i][j] == "":
#                     new_data[i].append("NaN")
#                 elif regex.search(data[i][j]):
#                     data[i][j] = re.sub('[" + pattern + "]', '', data[i][j])
#                     new_data[i].append(data[i][j])
#                 else:
#                     new_data[i].append(data[i][j])
#             else:
#                 if data[i][j] == "":
#                     new_data[i].append(0)
#                 elif regex.search(data[i][j]):
#                     data[i][j] = re.sub('[" + pattern + "]', '', data[i][j]) #replace data
#                     new_data[i].append(data[i][j])
#                 else:
#                     new_data[i].append(data[i][j])


# path1_data = getBufferData(Order Month) #month
# path2_data = getBufferData(Order Year) #year

# new_data = []
# new_head = []


# for i in range(0, len(path1_data)):
#     new_data.append([])
#     for j in range(9):
#         if j < 2:
#             new_data[i].append(path2_data[i][j])
#         elif 2 <= j <= 4
#             new_data[i].append(path1_data[i][j])
#         elif 5 <= j
#             new_data[i].append(path2_data[i][j - 3])
#     new_head = new_data[0]


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px
# from statsmodels.tsa.statespace.sarimax import SARIMAX
# from statsmodels.graphics.tsaplots import plot_acf,plot_pacf 
# from statsmodels.tsa.seasonal import seasonal_decompose 
# import warnings
# warnings.filterwarnings('ignore')
# plt.style.use('ggplot')
# df = pd.read_csv('OrdersandDeliveries.csv')
# df.head()

# df = df.drop(['Unfilled Orders'], axis = 1)
# df.info()

# df_new = df.dropna()

# df.replace(',','', regex=True, inplace=True)

# df['Order Total'] = pd.to_numeric(df['Order Total'])
# df['Delivery Total'] = pd.to_numeric(df['Delivery Total'])

# df.info()

# import missingno as msno
# msno.matrix(df)

# px.histogram(df, x='Engine',title='Frequency of engine type', text_auto='.2s')

# fig = px.pie(df, names='Engine', title = 'Population of Engine type')
# fig.show()

# df['Model Series'].value_counts().iloc[:5]

# plt.figure(figsize=(16,10))
# ax = df['Model Series'].value_counts().iloc[:5].plot(kind="bar", color = 'red')
# ax.title.set_text('Top 10 Causes For Canine Death')
# px.histogram(df, x='Region', color="Engine" ,title='Frequency of Region')
# plt.show()



# print("\n" + "*" * 20 + bc.BOLD + bc.HEADER + "FILE CSV HADING PROGRAM" + bc.ENDC + "*" * 20)
# print("-" * 18 + bc.HEADER + "The fuctions of the program" + bc.ENDC + "-" * 18)
# print("|\t\t\tEnter (" + bc.OKBLUE  + "1"  + bc.ENDC + ") :  " + bc.WARNING + "{0:38s}".format("Display data") + bc.ENDC + "|")
# print("|\t\t\tEnter (" + bc.OKBLUE  + "2"  + bc.ENDC + ") :  " + bc.WARNING + "{0:38s}".format("Merge data") + bc.ENDC + "|")
# print("|\t\t\tEnter (" + bc.OKBLUE  + "3"  + bc.ENDC + ") :  " + bc.WARNING + "{0:38s}".format("Display data was merge") + bc.ENDC + "|")
# print("|\t\t\tEnter (" + bc.OKBLUE  + "4"  + bc.ENDC + ") :  " + bc.WARNING + "{0:38s}".format("Clean data") + bc.ENDC + "|")
# print("|\t\t\tEnter (" + bc.OKBLUE  + "5"  + bc.ENDC + ") :  " + bc.FAIL + "{0:38s}".format("Exit") + bc.ENDC + "|")
# print("-" * 64)
# choice = int(input("> Enter your Choice: "))



