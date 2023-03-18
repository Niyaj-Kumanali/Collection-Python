from matplotlib import pyplot as plt

x = [10,30,50,20,50]
names = ['ten','thirty','fifty','twenty','fifty']
plt.pie(x , shadow=True, explode = [0,0,0,0.1,0], startangle=100, autopct='%1.1f%%',
        wedgeprops={'edgecolor' : 'green'}, labels = names)
plt.show()



# shadow = True for the enabling the shadows by default it is False
# explode = [] for seperating a block from pie chart len(x)==len(explode)
# startangle = 100 for rotating the pie chart anticlockwise by default it is 0
# colors = [] for specifying the colors
# autopct = '%1.1f%%' for specifying the percentage of each block the '%1.1f%%' is string code for percentage
# labels = [] for specifying the name/label for each block