import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

biao_ming=['task1-1A.csv','task1-1B.csv','task1-1C.csv','task1-1D.csv','task1-1E.csv']
for v in range(len(biao_ming)):


    data_all = pd.read_csv(biao_ming[v],encoding='gbk')
    data_all['支付时间'] = pd.to_datetime(data_all['支付时间'])#将日期时间转换为标准形式
    #data_all = data_all.set_index('支付时间')#将时间换位index格式

    #销量排名
    xiaoliangpaiming_C=data_all.groupby('商品').count()
    xiaoliangpaiming_C=xiaoliangpaiming_C.sort_values(by='订单号',ascending= False)
    xiaoliangpaiming_C=xiaoliangpaiming_C['订单号']
    xiaoliangpaiming_C.columns =['销量']
    #print(xiaoliangpaiming_C)

    #利润率排名
    fen_lei_biao_zhun=pd.read_csv('fu_jian_2.csv',encoding='gbk')
    mao_li_run=0
    #读取饮料类
    yin_liao_lei=[]
    for i in range(fen_lei_biao_zhun.loc[fen_lei_biao_zhun['大类'] == '饮料'].shape[0]):
        yin_liao_lei.append(fen_lei_biao_zhun.loc[fen_lei_biao_zhun['大类'] == '饮料'].reset_index(drop=True)['商品'][i])
    #print(yin_liao_lei)
    #读取非饮料类
    fei_yin_liao_lei=[]
    for i in range(fen_lei_biao_zhun.loc[fen_lei_biao_zhun['大类'] == '饮料'].shape[0]):
        fei_yin_liao_lei.append(fen_lei_biao_zhun.loc[fen_lei_biao_zhun['大类'] == '饮料'].reset_index(drop=True)['商品'][i])
    #print(fei_yin_liao_lei)


    #lirunlvpaiming_C=data_all.groupby('商品').count()
    maolirunpaiming_C=data_all
    maolirunpaiming_C=maolirunpaiming_C[['商品','应付金额']]#取所用列
    maolirunpaiming_C=maolirunpaiming_C.groupby('商品').sum()#通过商品进行分类并加和

    maolirunpaiming_C['毛利率']=0.20#新建毛利率列默认为0.2，非饮料类
    for i in range(maolirunpaiming_C.shape[0]):#如果是饮料，毛利率设为0.25
        if maolirunpaiming_C.iloc[i,0] in yin_liao_lei:
            maolirunpaiming_C.iloc[i,1]=0.25
        else :
            xxxx=1
    maolirunpaiming_C['商品总毛利润']=maolirunpaiming_C['应付金额']*maolirunpaiming_C['毛利率']#总毛利润=总销售额*毛利率
    maolirunpaiming_C=maolirunpaiming_C['商品总毛利润']#提取总毛利率
    #print(maolirunpaiming_C)

    zong=pd.merge(xiaoliangpaiming_C,maolirunpaiming_C,on='商品')
    zong.columns=['销量','商品总毛利润']
    zong['评价']=zong['销量']*0.6+zong['商品总毛利润']*0.4
    zong=zong.sort_values(by="评价",ascending= False)  

    zong['销售情况']=str(0)
    for i in range(zong.shape[0]):
        if i < zong.shape[0]*(0.5/10):
            zong['销售情况'][i]='热销'
        elif i<zong.shape[0]*(7/10):
            zong['销售情况'][i]='正常'
        else:
            zong['销售情况'][i]='滞销'
    #print(zong)

    ming_ming=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
    zong.to_csv('task3-1{name}.csv'.format(name=str(ming_ming[v])),encoding='gbk') #不保存行索引,编码格式为gbk