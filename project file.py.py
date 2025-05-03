#start the first wedge at 90 degrees
#the startangle parameter is defined with an angle in degrees,default angle is o:
#pie chart
import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
mylabels=["apples","bananas","cherries","dates"]

plt.pie(y,labels=mylabels,startangle=90)
plt.show()

#A histagram is a graph showing frequency distributions
#It is a graph showing the number of observations within each given interval.
#example:say you ask for the height of 250 people,you might end up with a histogram like this:
import matplotlib.pyplot as plt
import numpy as np

x=np.random.normal( loc=:170,scale=10,size=250)
plt.hist(x)
plt.show()

#use the numpy median() method to find the middle value:
import numpy

speed=[99,86,87,88,111,86,103,87,94,78,77,85,86]
x=numpy.median(speed)
print(x)