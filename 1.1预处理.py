import pandas as pd
data_all = pd.read_csv('fu_jian_1.csv',encoding='gbk')
#print(data_all.shape)

#处理设备ID
data_all['设备ID']=data_all['设备ID'].str[-5:]
#print(data_all)
#去除数据中应付金额为0的数据
data_all = data_all[data_all['应付金额'] != 0]
print(data_all)
#合并附件1和附件2至附件
data_all_1 = data_all
data_all_2 = pd.read_csv('fu_jian_2.csv',encoding='gbk')

fu_jian=pd.merge(data_all_1,data_all_2,on='商品')
fu_jian['设备ID']=fu_jian['设备ID'].str[-5:]


fu_jian.to_csv('fu_jian.csv',index=0,encoding='gbk') #不保存行索引,编码格式为gbk
print(fu_jian)
#查找所有设备id
she_bie_id=[]
for i in range(fu_jian.shape[0]):
    if fu_jian['设备ID'][i] in she_bie_id:
        xxxx=1
    else:
        she_bie_id.append(fu_jian['设备ID'][i])
print(she_bie_id)

#查找每个设备卖出的订单
ge_she_bei_ding_dan=[[] for i in range (len(she_bie_id))]
for i in range(len(she_bie_id)):
    ge_she_bei_ding_dan[i].append(fu_jian[fu_jian['设备ID'].isin([she_bie_id[i]])])
#print(ge_she_bei_ding_dan)
#print(ge_she_bei_ding_dan[0])

#将各设备订单另存为csv文件
ming_ming=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
for i in range(len(she_bie_id)):
    she_bei_biao=(ge_she_bei_ding_dan[i])[0]
    she_bei_biao.to_csv('task1-1{name}.csv'.format(name=str(ming_ming[i])),index=0,encoding='gbk') #不保存行索引,编码格式为gbk




