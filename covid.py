import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv(r'C:\Users\ARAVIND\Downloads\Madedata3.csv')
le=LabelEncoder()
le.fit_transform(['Female','Male'])
df['Gender']=df['Gender'].map({'Female':0,'Male':1,'Transgender':2})
df['Severity'].value_counts()
le.fit_transform(['Mild','Moderate','Severe'])
df['Severity']=df['Severity'].map({'Mild':0,'Moderate':1,'Severe':2})
df['Contact_with_covid_patient'].value_counts()
le.fit_transform(['No','Yes','Not known','yes'])
df['Contact_with_covid_patient']=df['Contact_with_covid_patient'].map({'No':0,'Yes':1,'Not known':2,'yes':1})
X=df[['Contact_with_covid_patient','Age','Bodypain','Severity','Difficulty_in_breathing']]
y=df['Infected']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.8,random_state=0)
from sklearn.tree import DecisionTreeClassifier
de=DecisionTreeClassifier()
de.fit(X_train,y_train)
de_predict=de.predict(X_test)
# Saving model to disk
pickle.dump(de, open('model2.pkl','wb'))

# Loading model to compare the results
f = open('model2.pkl','rb')
model2=pickle.load(f)