#计算每台售货机的交易额的月环比增长率并画柱状图
import pandas as pd
import matplotlib.pyplot as plt
suo_you_ji_qi_de_jiao_yi_zong_e=[]


biao_ming=['task1-1A.csv','task1-1B.csv','task1-1C.csv','task1-1D.csv','task1-1E.csv']
for i in range(len(biao_ming)):
    wen_jian_ming=biao_ming[i]
    data_all = pd.read_csv(wen_jian_ming,encoding='gbk')
    #print(data_all)

    data_all['支付时间'] = pd.to_datetime(data_all['支付时间'])#将日期时间转换为标准形式
    data_all = data_all.set_index('支付时间')#将时间换位index格式
    #print(data_all)


    zong_jiao_yi_e=[]#创建存储总交易额的空列表

    tong_ji_jie_guo=data_all.resample('MS').sum()#根据每月进行统计

    #print(tong_ji_jie_guo['实际金额'][0])

    for i in range(tong_ji_jie_guo.shape[0]):
        zong_jiao_yi_e.append(float('%.2f'% tong_ji_jie_guo['实际金额'][i]))#获得每月实际金额取小数点后两位放入列表中
    suo_you_ji_qi_de_jiao_yi_zong_e.append(zong_jiao_yi_e)

yue_fen=['{name}月'.format(name=str(i+2)) for i in range(11)]#设定月份,由于月环比增长率从第二开始计算，特此设置
yue_huan_bi_zeng_zhang_lv=[]
suo_you_ji_qi_de_yue_huan_bi_zeng_zhang_lv=[]

#print(yue_fen)
#print(suo_you_ji_qi_de_jiao_yi_zong_e)
#计算获得所有月环比增长率
for i in range(len(suo_you_ji_qi_de_jiao_yi_zong_e)):
    for j in range(len(suo_you_ji_qi_de_jiao_yi_zong_e[i])-1):
        zeng_zhang_lv=((suo_you_ji_qi_de_jiao_yi_zong_e[i])[j]-(suo_you_ji_qi_de_jiao_yi_zong_e[i])[j-1])/(suo_you_ji_qi_de_jiao_yi_zong_e[i])[j-1]
        yue_huan_bi_zeng_zhang_lv.append(zeng_zhang_lv)
        #print(yue_huan_bi_zeng_zhang_lv)
    suo_you_ji_qi_de_yue_huan_bi_zeng_zhang_lv.append(yue_huan_bi_zeng_zhang_lv)
    yue_huan_bi_zeng_zhang_lv=[]
    #print(len(suo_you_ji_qi_de_yue_huan_bi_zeng_zhang_lv))


#画图
for i in range(5):
    # 构建数据
    x_data = yue_fen
    y_data = suo_you_ji_qi_de_yue_huan_bi_zeng_zhang_lv[i]
    # 绘图
    plt.bar(x=x_data, height=y_data, label='第{name}台的月环比增长率'.format(name=str(i+1)), color='steelblue', alpha=0.8)

    # 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
    for x, y in enumerate(y_data):
        plt.text(x, y , '%.2f'% y, ha='center', va='bottom')

    # 设置标题
    plt.title('第{name}台的每月环比增长率'.format(name=str(i+1)))
    # 为两条坐标轴设置名称
    plt.xlabel("月份")
    plt.ylabel("月环比增长率")
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    # 显示图例
    plt.legend()
    plt.show()

