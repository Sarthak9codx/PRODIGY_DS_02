         Titanic Dataset- Data Cleaning and EDA(Exploratory Data Analysis)

Step 1:
       To clean the Titanic dataset and explore patterns in Survival based.
   
Data Cleaning 
1: Handled Missing values.
  .Age: Filled with median age>.
  .Embarked: Filled with most value(mode).
  .Cabin: Used Droped function to drop because to many values are lost.

2:Converted Categorical Data to Numeric:
  >Sex:"male"->0, "female"->1.
  >Embarked:'S'->0, 'C'->1,'Q'->2.

Step2:
    Visual Analysis(EDA).
1.Survival Rate by Gender.
  > Bar plot shows females had a higher survival rate then males.

2.Survival Rate by Pclass.
 >Survival chance was highest in 1st class and lowest in 3rd class.
 >use Barplot.

3.Age Distribution
 >Histogram used to show the distribution of passenger ages.
 >Most passengers were between 20-40 years old.

4.Age vs Survival
  >Boxplot shows survivors were generally younger.



After Analysis Data 
  >Females had better survival chances.
  >1st class passengers had higher survival than others.
  >Younger passengers had a slightly better survival chance.
