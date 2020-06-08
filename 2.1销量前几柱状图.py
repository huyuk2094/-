import pandas as pd
import matplotlib.pyplot as plt
data_all = pd.read_csv('fu_jian_1.csv',encoding='gbk')

#处理设备ID
data_all['设备ID']=data_all['设备ID'].str[-5:]

#时间处理
data_all['支付时间'] = pd.to_datetime(data_all['支付时间'])#将日期时间转换为标准形式
data_all = data_all.set_index('支付时间')#将时间换位index格式

xx=input('请输入要绘制那一月的销量柱状图,格式:2017-06\n')
data_use=data_all[xx]#获取当月数据
#print(data_use)

#遍历得到所有商品名单
shang_pin_ming_dan=[]
for i in range(data_all.shape[0]):
    if data_all['商品'][i] in shang_pin_ming_dan:
        xxxx=1
    else:
        shang_pin_ming_dan.append(data_all['商品'][i])
#print(shang_pin_ming_dan)#得到商品名字的列表 
xiao_liang=[0 for i in range (len(shang_pin_ming_dan))]#创建同长的0列表
shang_pin_xiao_liang_biao=dict(zip(shang_pin_ming_dan,xiao_liang))#名字和数量，两个列表压缩为字典
#print(shang_pin_xiao_liang_biao)

#遍历计算商品销量
#print(shang_pin_xiao_liang_biao[data_use[1][6]])
for i in range(data_use.shape[0]):
    shang_pin_xiao_liang_biao[data_use['商品'][i]]=shang_pin_xiao_liang_biao[data_use['商品'][i]]+1
#print(shang_pin_xiao_liang_biao)
shang_pin_xiao_liang_biao = sorted(shang_pin_xiao_liang_biao.items(),key=lambda d:d[1],reverse=True)#按值从大到小排序
#print(shang_pin_xiao_liang_biao)

#绘图
yy=int(input('请输入要绘制销量前几的柱状图,格式:2\n'))
ming_cheng=[]
xiao_liang_lie_biao=[]
for i in range(yy):
    ming_cheng.append(shang_pin_xiao_liang_biao[i][0])
    xiao_liang_lie_biao.append(shang_pin_xiao_liang_biao[i][1])
#print(ming_cheng)
#print(xiao_liang_lie_biao)

x_data =ming_cheng
y_data =xiao_liang_lie_biao
plt.bar(x=x_data, height=y_data, color='steelblue')
for x, y in enumerate(y_data):
    plt.text(x, y + 5, '%s' % y, ha='center', va='bottom')
plt.title('销量前{name}的商品'.format(name=str(yy)))
plt.xlabel("商品")
plt.ylabel("销量")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 显示图例
plt.legend()
plt.show()