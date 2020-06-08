import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data_all = pd.read_csv('task1-1C.csv',encoding='gbk')
data_all['支付时间'] = pd.to_datetime(data_all['支付时间'])#将日期时间转换为标准形式
data_all = data_all.set_index('支付时间')#将时间换位index格式
#print(data_all)

#6月
data_6=(data_all['2017-06'])['订单号']
#print(data_6.resample('H').count())#按小时排序

a_6=data_6.resample('H').count().tolist()
b_6=[[] for i in range(30)]
#print(aa)

for i in range(30):
    z=0
    for j in range(int(30)):
        b_6[z]=a_6[0+23*j:24+23*j]
        z=z+1
#print(b_6)

c_6_1 = np.array(b_6).T
c_6_2 = pd.DataFrame(c_6_1)

ri_qi_6_yue=['{name}日'.format(name=str(i+1)) for i in range(30)]#获得每月日期
shi_jian=['{name}点'.format(name=str(i+1)) for i in range(24)]#获得每天时间

c_6_2.columns = ri_qi_6_yue
c_6_2.index=shi_jian
#print(c_6_2)

#7月
data_7=(data_all['2017-07'])['订单号']
#print(data_6.resample('H').count())#按小时排序

a_7=data_7.resample('H').count().tolist()
b_7=[[] for i in range(31)]
#print(aa)

for i in range(31):
    z=0
    for j in range(int(31)):
        b_7[z]=a_7[0+24*j:24+24*j]
        z=z+1
#print(b_7)
c_7_2 = pd.DataFrame(b_7).T
c_7_2=c_7_2.fillna(0)
#print(c_7_2)
ri_qi_7_yue=['{name}日'.format(name=str(i+1)) for i in range(31)]#获得每月日期
shi_jian=['{name}点'.format(name=str(i+1)) for i in range(24)]#获得每天时间
#print(c_7_2)
c_7_2.columns = ri_qi_7_yue
c_7_2.index=shi_jian
#print(c_7_2)

#8月
data_8=(data_all['2017-08'])['订单号']
#print(data_6.resample('H').count())#按小时排序

a_8=data_8.resample('H').count().tolist()
b_8=[[] for i in range(31)]
#print(aa)

for i in range(31):
    z=0
    for j in range(int(31)):
        b_8[z]=a_8[0+24*j:24+24*j]
        z=z+1
#print(b_8)
c_8_2 = pd.DataFrame(b_8).T
c_8_2=c_8_2.fillna(0)

#print(c_8_2)
ri_qi_8_yue=['{name}日'.format(name=str(i+1)) for i in range(31)]#获得每月日期
shi_jian=['{name}点'.format(name=str(i+1)) for i in range(24)]#获得每天时间
#print(c_8_2)
c_8_2.columns = ri_qi_8_yue
c_8_2.index=shi_jian
#print(c_8_2)

# 初始化参数
plt.figure(figsize=(12,8))
heatmap = sns.heatmap(c_6_2.values, annot=True,cmap="Blues_r")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.xlabel("天")
plt.ylabel("小时")
plt.title('六月份销量热力图')
plt.show()

plt.figure(figsize=(12,8))
heatmap = sns.heatmap(c_7_2.values, annot=True,cmap='PuBu')
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.xlabel("天")
plt.ylabel("小时")
plt.title('七月份销量热力图')
plt.show()

plt.figure(figsize=(12,8))
heatmap = sns.heatmap(c_8_2.values, annot=True,cmap="Greens")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.xlabel("天")
plt.ylabel("小时")
plt.title('八月份销量热力图')
plt.show()
