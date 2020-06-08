import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
data_all = pd.read_csv('fu_jian.csv',encoding='gbk')

data_all['支付时间'] = pd.to_datetime(data_all['支付时间'])#将日期时间转换为标准形式
data_all = data_all.set_index('支付时间')#将时间换位index格式

grouped = (data_all['实际金额'].groupby(data_all['二级类'])).sum()#通过groupby来分组操作 

#获得每个月的二级类的销量
yiyue=data_all['2017-01']
eryue=data_all['2017-02']
sanyue=data_all['2017-03']
siyue=data_all['2017-04']
wuyue=data_all['2017-05']
liuyue=data_all['2017-06']
qiyue=data_all['2017-07']
bayue=data_all['2017-08']
jiuyue=data_all['2017-09']
shiyue=data_all['2017-10']
shiyiyue=data_all['2017-11']
shieryue=data_all['2017-12']

yiyue_sum=(yiyue['实际金额'].groupby(yiyue['二级类'])).sum()
eryue_sum=(eryue['实际金额'].groupby(eryue['二级类'])).sum()
sanyue_sum=(sanyue['实际金额'].groupby(sanyue['二级类'])).sum()
siyue_sum=(siyue['实际金额'].groupby(siyue['二级类'])).sum()
wuyue_sum=(wuyue['实际金额'].groupby(wuyue['二级类'])).sum()
liuyue_sum=(liuyue['实际金额'].groupby(liuyue['二级类'])).sum()
qiyue_sum=(qiyue['实际金额'].groupby(qiyue['二级类'])).sum()
bayue_sum=(bayue['实际金额'].groupby(bayue['二级类'])).sum()
jiuyue_sum=(jiuyue['实际金额'].groupby(jiuyue['二级类'])).sum()
shiyue_sum=(shiyue['实际金额'].groupby(shiyue['二级类'])).sum()
shiyiyue_sum=(shiyiyue['实际金额'].groupby(shiyiyue['二级类'])).sum()
shieryue_sum=(shieryue['实际金额'].groupby(shieryue['二级类'])).sum()
#十二个月合并
res = pd.concat([yiyue_sum,eryue_sum,sanyue_sum,siyue_sum,wuyue_sum,liuyue_sum,qiyue_sum,bayue_sum,jiuyue_sum,shiyue_sum,shiyiyue_sum,shieryue_sum],axis=1)
#print(res)
#空缺值处理

res=res.fillna(0)
#print(res)

#获得月份
yue_fen=['{name}月'.format(name=str(i+1)) for i in range(12)]#设定月份
#处理列名
res.columns = yue_fen
print(res)

x = [i for i in range(12)]
y = [i for i in range(20)]
xx , yy = np.meshgrid(x,y)
# print(xx)
# print(yy)
plt.figure(figsize=(10, 10))
plt.scatter(xx,yy,s=res.values/20)
plt.xticks(x,res.columns)
plt.yticks(y,res.index)
plt.title('每月交易额均值气泡图')
plt.show()







