import pandas as pd
import matplotlib.pyplot as mb
import seaborn as sb
titi=pd.read_csv("C:\\titanic\\train.csv")

#Reading Data
print(titi.isnull().sum())


#Data cleanig 
titi["Age"].fillna(titi["Age"].median(),inplace=True)

titi.drop(columns=["Cabin"],inplace=True)

titi["Embarked"].fillna(titi["Embarked"].mode()[0],inplace=True)


#Converting data or modiyfing data
titi["Sex"]=titi["Sex"].map({"male":0,"female":1})
titi["Embarked"]=titi["Embarked"].map({'S':0,'C':1,'Q':2})
print(titi["Survived"].value_counts(normalize=True))


#Survived throug Sex in Bargraph plot
sb.barplot(x="Sex",y="Survived",data=titi,palette=["Red","LightPink"])
mb.title("Survived Rate by Sex")
mb.xticks([0,1],["Male","Female"])
mb.show()

#Survived by Pc class
sb.barplot(x="Pclass",y="Survived",data=titi,palette="Set2")
mb.title("Survived Rate by Pclass")
mb.xticks([0,1,2],["S","C","Q"])
mb.show()

#Age Distribution
sb.histplot(titi["Age"],bins=30,color="orange")
mb.title("Age Distribution")
mb.show()

#Age vs Survival
sb.boxplot(x="Survived",y="Age",data=titi,palette=["Orange","Blue"])
mb.title("Age vs Survival")
mb.show()