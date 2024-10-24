
#numpy
import numpy as np


a=np.array([1,2,3])
b=np.array([['a','b'],['c','d']])
print("Array a: ",a)
print("Array b: ",b)
print("Type of a: ",type(a))
print("Type of b: ",type(b))
print("Data type of a: ",a.dtype)
print("Data type of b: ",b.dtype)
print("Number of dimensions of a: ",a.ndim)
print("Number of dimensions of b: ",b.ndim)
print("Size of a: ",a.size)
print("Size of b: ",b.size) 
print("Shape of a: ",a.shape)
print("Shape of b: ",b.shape)


a=np.zeros((3,3))
print(a)
a=np.ones((3,3))
print(a)
a=np.arange(0,10)
print(a)
a=np.arange(4,10)
print(a)
a=np.arange(0,12,3)
print(a)
a=np.arange(0,6,0.5)
print(a)
a=np.arange(0,12).reshape(3,4)
print(a)
a=np.linspace(0,10,5)
print(a)
a=np.random.random(3)
print(a)
a=np.random.random((3,3))
print(a)


a=np.arange(5)
print("a = ",a)
print("a+4= ",a+4)
print("a*2= ",a*2)
b=np.arange(5,10)
print("b = ",b)
print("a+b= ",a+b)
print("a-b= ",a-b)
print("a*b= ",a*b)



a=np.arange(0,9).reshape(3,3)
b=np.arange(5,14).reshape(3,3)
print("a:")
print(a)
print("b:")
print(b)
print("a*b:")
print(a*b)
print("dot ab:")
print(np.dot(a,b))
print("dot ba:")
print(np.dot(b,a))


a=np.arange(4)
print(a)
a+=5
print(a)
a-=2
print(a)
a*=2
print(a)


a=np.arange(1,5)
print(a)
print(np.sqrt(a))
print(np.log(a))
print(np.sin(a))


a=np.array([3,5,2,7,10,8])
print(a)
print(a[3])
print(a[-1])
print(a[-4])
print(a[[2,4,5]])


a=np.array([[3,5,2,7,10,8],[12,18,14,16,15,20],[26,22,30,24,25,28]])
print(a)
print(a[2,5])
print(a[-1,-1])
print(a[-2,3])
print(a[0,-1])

a=np.arange(10,21)
print(a)
print(a[1:8])
print(a[1:])
print(a[:5])
print(a[1:8:2])
print(a[1:8:3])
print(a[::2])
print(a[:5:2])


a=np.arange(10,19).reshape(3,3)
print(a)
print(a[0,1])
print(a[0,:])
print(a[:,0])
print(a[0:2,0:2])
print(a[[0,2],:2]) #row 0 and 2, 
#column up to 2

a=np.arange(10,19).reshape(3,3)
for i in a.flat:
 print(i)

a=np.arange(10,19).reshape(3,3)
print(np.apply_along_axis(np.sum,axis=1,arr=a))
#axis=0 means add values horizontally
#axis=1 means add values vertically
print(a)
print(a<15)
print(a[a<15])

marks=np.array([50,70,60,40,80,90])
np.savetxt('marks.csv', marks, delimiter=',')


#pandas
import pandas as pd
import openpyxl as xl

s=pd.Series([20,15,18,10,12])
print(s)

s=pd.Series([20,15,18,10,12],index=['a','b','c','d','e'])
print(s)

arr=np.arange(5,10)
s=pd.Series(arr)
print(s)

s=pd.Series([5,7,9,3,8])
print(s)
s1=pd.Series(s)
print(s1)
s[2]=25
print(s1)


s=pd.Series([10,20,40],index=['a','b','c'])

print(s)
s['b']=40
print(s)
print(s.unique())
print(s.value_counts())

print(s.isin([40]))

s=pd.Series([5,4,np.nan,3])
print(s)
print(s.isnull())
print(s.notnull())
print(s[s.notnull()])
print(s[s.isnull()])


marks={'Kumara':80,'Kumari':75,'Ravi':60,'Rani':50}
s=pd.Series(marks)
print(s)

marks={'Kumara':80,'Kumari':75,'Ravi':60,'Rani':50}
students=['Kumara','Gamini','Kumari','Ravi','Rani']
s=pd.Series(marks,index=students)
print(s)


#DataFrame in Pandas

data={'Name':['Kumara','Kumari','Ravi','Rani'],
 'Marks':[56,67,89,50]}
marks=pd.DataFrame(data)
marks.to_excel('marks1.xlsx')



data={'Name':['Kumara','Kumari','Ravi','Rani','Gamini'],
      'Department':['Administration','Finance','Marketing','Finance','Administration'],
      'Salary':[150000,130000,135000,140000,160000],
      'Experience':[2,3,4,5,7]}
emp=pd.DataFrame(data,columns=['Name','Department','Salary'],index=['E01','E02','E03','E04','E05'])
print(emp)
print(emp.isnull())
print(emp.columns)
print(emp.head(3))
print(emp.index)
print(emp.values)
print(emp['Salary'])
print(emp.Salary)
print(emp.iloc[2])
print(emp.iloc[1,0])#0 for column(Name),1 for index inside column(Kumari)
print(emp[0:2])
#print(emp['Name'][2])#2 for index (2-ravi) inside name column
print(emp.loc['E03'])


emp.index.name='ID'
emp.columns.name='Employee'
emp['Role']=['Coordinator','Audit','Graphics Designer','Assistent Accountant','Front Officer']
emp['Leave in Auguest']=[2,5,6,1,3]
print(emp.isin(['Coordinator','Audit']))
del emp['Leave in Auguest']
print(emp)
print(emp.Department=='Finance')
print(emp[emp.Department=='Finance'])
print(emp[emp.Salary<=140000])
print(emp.T)


a=np.array([[8,10,7,3],[12,15,6,10],[7,3,7,11],[3,6,7,12]])
frame1=pd.DataFrame(a,index=['red','blue','yellow','white'],
 columns=['ball','pen','pencil','paper'])
b=np.array([[4,6,8,5],[12,14,5,8],[4,12,8,9],[6,8,10,9]])
frame2=pd.DataFrame(b,index=['red','blue','yellow','white'],
 columns=['ball','pen','pencil','paper'])
print(frame1)
print()
print(frame1.sum())#sum by labels
print(sum(frame1['ball']))
#sum of balls
print(frame1.mean())#mean by labels
print(frame1.describe())#count,mean,sd,min,25%,50%,75%,max by labels
#print(frame1.corr())
#print(frame1.cov())
#print(frame1.corrwith(frame2))


set1=pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
 'color':['white','red','red','black','green'],
 'brand':['OMG','ABC','ABC','POD','POD']})
print(set1)
set2=pd.DataFrame({'id':['pencil','pencil','ball','pen'],
 'brand':['OMG','POD','ABC','POD']})
print(set2)
print(pd.merge(set1,set2,on='brand'))
print(pd.merge(set1,set2,on='id',how='left'))
print(pd.merge(set1,set2,on='id',how='right'))
print(pd.merge(set1,set2,on='id',how='outer'))


#Matplotlib
import matplotlib.pyplot as plt


year=['2015','2016','2017','2018','2019']
income=np.array([250000,300000,280000,320000,340000])
expenses=np.array([180000,200000,250000,260000,270000])
profit=income-expenses
plt.title('Income Expenses and Profit By Years',fontsize=20,fontname='Times New Roman',color= 'green')
plt.xlabel('Years',color='blue')
plt.ylabel('Values in rupees',color='blue')
plt.grid(True)
plt.plot(year,income,'ro',color='green')#can use symbols instead on lines
plt.plot(year,expenses,'y^',color='red')
plt.plot(year,profit,color='blue')
plt.legend(['Income','Expenses','Profit'],loc=2)
plt.show()


data={'Month':['Jan','Feb','Mar','Apr','May','Jun'],
 'Income':[450000,380000,400000,420000,450000,470000],
 'Expenses':[350000,360000,370000,370000,380000,385000]}

df=pd.DataFrame(data)
plt.plot(df.Month,df.Income,df.Month,df.Expenses)
plt.show()


month=['Jan','Feb','Mar','Apr','May','Jun']
income=[450000,280000,100000,320000,400000,470000]
expenses=[180000,200000,250000,260000,270000]

plt.bar(month,income)
plt.show()

plt.barh(month,income)
plt.show()


Year=np.arange(2015,2020)
Income=np.array([250000,300000,280000,320000,340000])
Expenses=np.array([180000,200000,250000,260000,270000])
Profit=Income-Expenses
bw=0.3#Bar width
plt.bar(Year,Income,bw,color='green')
plt.bar(Year+bw,Expenses,bw,color='red')
plt.bar(Year+2*bw,Profit,bw,color='blue')
plt.xlabel('Year')
plt.ylabel('Amount in USD')
plt.title('Income, Expenses, and Profit from 2015 to 2019')
plt.xticks(Year + bw, Year)  # Adjust the x-axis ticks to align with bars
plt.legend(['Income','Expenses','Profit'],loc=2)
plt.show()


data={'Month':['Jan','Feb','Mar','Apr','May','Jun'],
 'Income':[450000,380000,400000,420000,450000,470000],
 'Expenses':[350000,360000,370000,370000,380000,385000]}
df=pd.DataFrame(data,index=['Jan','Feb','Mar','Apr','May','Jun'])
df['profit']=df.Income-df.Expenses
df.plot(kind='bar')
plt.show()


faculties=['Manegement','Art','Science','Medical','Engineering','Technology']
students=[5400,3200,1500,1800,400,600]
colors=['yellow','green','red','blue','brown','orange']
explode=[0,0.1,0,0,0,0]
plt.pie(students,labels=faculties,colors=colors,explode=explode)
plt.show()


xs=np.random.randint(30,40,100)
ys=np.random.randint(20,30,100)
xs2=np.random.randint(50,60,100)
ys2=np.random.randint(30,40,100)
xs3=np.random.randint(10,30,100)
ys3=np.random.randint(40,50,100)
#ax=plt.axes(projection='3d') #to create 3D scatter plot
plt.scatter(xs,ys)#if 3D scatter plot, we have to give 3 arrays to each scatter group
plt.scatter(xs2,ys2,c='r',marker='^')
plt.scatter(xs3,ys3,c='g',marker='*')
plt.show()
