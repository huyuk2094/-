#计算每台售货机的占总毛利润的饼图
import pandas as pd
import matplotlib.pyplot as plt

mao_li_run=0
mao_li_run_hui_zong=[]
#读取分类标准
fen_lei_biao_zhun=pd.read_csv('fu_jian_2.csv',encoding='gbk')
#print(fen_lei_biao_zhun.head(3))

biao_ming=['task1-1A.csv','task1-1B.csv','task1-1C.csv','task1-1D.csv','task1-1E.csv']
for i in range(len(biao_ming)):
    wen_jian_ming=biao_ming[i]
    data_all = pd.read_csv(wen_jian_ming,encoding='gbk')

    #print(data_all.head(3))

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

    for i in range(data_all.shape[0]):
        if data_all['商品'][i] in  yin_liao_lei:
            mao_li_run=mao_li_run+data_all['应付金额'][i]*0.25
        else:
            mao_li_run=mao_li_run+data_all['应付金额'][i]*0.20

    mao_li_run_hui_zong.append(float('%.2f'% mao_li_run))
print(mao_li_run_hui_zong)

#画图
# 准备数据
data = mao_li_run_hui_zong
# 准备标签
labels = biao_ming
# 将第4个语言（Python）分离出来
explode = [0.1 for i in range(len(biao_ming))]
# 使用自定义颜色
#colors=['red', 'pink', 'magenta','purple','orange']
# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.figure(figsize=(8, 8))
plt.axes(aspect='equal')
# 控制X轴和Y轴的范围（用于控制饼图的圆心，半径）
plt.xlim(0,5)
plt.ylim(0,5)
# 绘制饼图
plt.pie(x = data, # 绘图数据
    labels=labels, # 添加编程语言标签
    explode=explode, # 突出显示Python
    #colors=colors, # 设置饼图的自定义填充色
    autopct='%.3f%%', # 设置百分比的格式，此处保留3位小数
    pctdistance=0.8,  # 设置百分比标签与圆心的距离
    labeldistance = 1.15, # 设置标签与圆心的距离
    startangle = 180, # 设置饼图的初始角度
    center = (2.3, 2.3), # 设置饼图的圆心（相当于X轴和Y轴的范围）
    radius = 2, # 设置饼图的半径（相当于X轴和Y轴的范围）
    counterclock = False, # 是否逆时针，这里设置为顺时针方向
    wedgeprops = {'linewidth': 1, 'edgecolor':'green'},# 设置饼图内外边界的属性值
    textprops = {'fontsize':12, 'color':'black'}, # 设置文本标签的属性值
    frame = 1) # 是否显示饼图的圆圈，此处设为显示
# 不显示X轴和Y轴的刻度值
plt.xticks(())
plt.yticks(())
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
for x, y in enumerate(data):
    plt.text(y,x , '%.2f'% y, ha='center', va='bottom')
# 添加图标题
plt.title('各售卖机毛利润占比')
# 显示图形
plt.show()