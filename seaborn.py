# -*- coding: utf-8 -*-
"""Seaborn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pU29qQOVclgVghwsbu-EU8mJaEghwHbc
"""

pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
tips = sns.load_dataset("tips")
print(tips)
#create a scatter plot
sns.scatterplot(x="total_bill",y="tip",data=tips,label='dots')
plt.title("Scatter Plot of Total Bill vs.Tip")
plt.xlabel("Total Bill($)")
plt.ylabel("Tip($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
iris = sns.load_dataset("iris")
print(iris)
#create a scatter plot
sns.scatterplot(x="sepal_length",y="sepal_width",data=iris)
plt.title("Scatter Plot of sepal_length vs.sepal_width")
plt.xlabel("sepal_length($)")
plt.ylabel("sepal_width($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
tips = sns.load_dataset("tips")
print(tips)
#create a bar plot
sns.barplot(x="day",y="total_bill",data=tips,label='dots')
plt.title("Average total bill by day")
plt.xlabel("day of the week")
plt.ylabel("average total bill($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
tips = sns.load_dataset("tips")
print(tips)
#create a box plot
sns.boxplot(x="day",y="total_bill",data=tips)
plt.title("disrtibution of total bill by day")
plt.xlabel("day of the week")
plt.ylabel(" total bill($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
tips = sns.load_dataset("tips")
print(tips)
#create a violin plot
sns.violinplot(x="day",y="total_bill",data=tips)
plt.title("disrtibution of total bill by day")
plt.xlabel("day of the week")
plt.ylabel(" total bill($)")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
a=pd.read_csv("/content/grades_withnulls.csv")
b=sns.lineplot(x='Names',y='Grade',data=a)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
iris=sns.load_dataset("iris")
correlation_matrix=iris.corr()
sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm')
plt.title("correlation heatmap of iris dataset")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
tips = sns.load_dataset("tips")
print(tips)
#create a join plot
sns.jointplot(x="total_bill",y="tip",data=tips)
plt.title("scatter plot of total bill  vs.tip")
plt.xlabel("total bill($)")
plt.ylabel(" tips($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
titanic= sns.load_dataset("titanic")
print(titanic)
#create a count plot
sns.countplot(x="class",data=titanic)
plt.title("passenger class disrtibution")
plt.xlabel("class")
plt.ylabel("count")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
tips= sns.load_dataset("tips")
print(titanic)
#create a lm plot
sns.lmplot(x="total_bill",y='tip',data=tips)
plt.title("linear regression of total bill and tip")
plt.xlabel("total bill($)")
plt.ylabel("tip($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
titanic= sns.load_dataset("titanic")
print(titanic)
#create a facet grid of age distributions for diferent passenger classes
g=sns.FacetGrid(titanic,col='class')
g.map(sns.histplot,"age")
plt.subplots_adjust(top=0.8)
g.fig.suptitle("age disrtibution by passenger class")
plt.show()

