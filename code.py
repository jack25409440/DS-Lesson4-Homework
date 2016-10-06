import pandas as pd

def count_total_number_of_items(item1, item2, df):
    count1 = 0
    count2 = 0
    for index,row in df.iterrows():
        if item1 == row['item_name']:
            count1 += int(row['quantity'])
        if item2 == row['item_name']:
            count2 += int(row['quantity']) 
    return {item1:count1, item2:count2}
        

def number_of_items_with_material_in_list(material1, material2, df):
    count1 = 0
    count2 = 0
    for index,row in df.iterrows():
        if material1 in row['choice_description']:
            count1+=int(row['quantity'])
        if material2 in row['choice_description']:
            count2+=int(row['quantity'])
    return {material1:count1, material2:count2}

dataframe = pd.read_table("chipotle.tsv")

#Problem 2
print('Problem 2')
print "Number of orders: ", len(dataframe['order_id'].value_counts().index)
print

#Problem 3
print('Problem 3')
print "Number of lines: ", len(dataframe.index)
print

#Problem 4
print('Problem 4')
filtered_df = dataframe[(dataframe['item_name'] == 'Steak Burrito') | (dataframe['item_name'] == 'Chicken Burrito')][['quantity', 'item_name']]
number_of_steak_and_chicken_burritos = count_total_number_of_items('Steak Burrito', 'Chicken Burrito', filtered_df)
print(number_of_steak_and_chicken_burritos)
print 

#Problem 5
print('Problem 5')
chicken_burrito_df = dataframe.loc[lambda df : df['item_name'] == 'Chicken Burrito'][['choice_description', 'quantity']]
number_of_chicken_burrito_with_materials = number_of_items_with_material_in_list('Black Beans', 'Pinto Beans', chicken_burrito_df)
print(number_of_chicken_burrito_with_materials)
