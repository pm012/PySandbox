#Pie charts in python example
import matplotlib.pyplot as pyplot

labels = ('Python', 'Java', 'Scala','C#')
values_percentage = [45, 40, 15, 10]
pyplot.pie(values_percentage, labels=labels,
           autopct='%1.f%%',
           counterclock=False, startangle=90)

pyplot.show()
