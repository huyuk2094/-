#计算每台售货机的交易额并画折线图
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


    yue_fen=['{name}月'.format(name=str(i+1)) for i in range(12)]#设定月份
    zong_jiao_yi_e=[]#创建存储总交易额的空列表

    tong_ji_jie_guo=data_all.resample('MS').sum()#根据每月进行统计

    #print(tong_ji_jie_guo['实际金额'][0])

    for i in range(tong_ji_jie_guo.shape[0]):
        zong_jiao_yi_e.append(float('%.2f'% tong_ji_jie_guo['实际金额'][i]))#获得每月实际金额取小数点后两位放入列表中
    suo_you_ji_qi_de_jiao_yi_zong_e.append(zong_jiao_yi_e)


print(yue_fen)
print(suo_you_ji_qi_de_jiao_yi_zong_e)

x_data =yue_fen
# 定义2个列表分别作为两条折线的Y轴数据
y_data1 =suo_you_ji_qi_de_jiao_yi_zong_e[0]
y_data2 =suo_you_ji_qi_de_jiao_yi_zong_e[1]
y_data3 =suo_you_ji_qi_de_jiao_yi_zong_e[2]
y_data4 =suo_you_ji_qi_de_jiao_yi_zong_e[3]
y_data5 =suo_you_ji_qi_de_jiao_yi_zong_e[4]
# 指定折线的颜色、线宽和样式
plt.plot(x_data, y_data1, color = 'blue', linewidth = 1, marker='o', label='A售卖机' )
plt.plot(x_data, y_data2, color = 'green', linewidth = 1,marker='o', label='B售卖机')
plt.plot(x_data, y_data3, color = 'red', linewidth = 1,marker='o', label='C售卖机')
plt.plot(x_data, y_data4, color = 'cyan', linewidth = 1,marker='o', label='D售卖机')
plt.plot(x_data, y_data5, color = 'black', linewidth = 1,marker='o', label='E售卖机')

for x, y in enumerate(y_data1):
    plt.text(x, y + 20, '%s' % y, ha='center', va='bottom')
for x, y in enumerate(y_data2):
    plt.text(x, y + 20, '%s' % y, ha='center', va='bottom')
for x, y in enumerate(y_data3):
    plt.text(x, y + 20, '%s' % y, ha='center', va='bottom')
for x, y in enumerate(y_data4):
    plt.text(x, y + 20, '%s' % y, ha='center', va='bottom')
for x, y in enumerate(y_data5):
    plt.text(x, y + 20, '%s' % y, ha='center', va='bottom')



plt.title("每台售货机每月销售额")
plt.xlabel("月份")
plt.ylabel("销售额")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 调用show()函数显示图形
plt.legend()
plt.show()