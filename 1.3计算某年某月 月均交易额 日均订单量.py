import pandas as pd

#计算某年某月 月均交易额 日均订单量
biao_ming=['task1-1A.csv','task1-1B.csv','task1-1C.csv','task1-1D.csv','task1-1E.csv']
for i in range(len(biao_ming)):
    wen_jian_ming=biao_ming[i]
    print('现在进行的是对'+str(wen_jian_ming)+'的操作')
    data_all = pd.read_csv(wen_jian_ming,encoding='gbk')
    #print(data_all)

    data_all['支付时间'] = pd.to_datetime(data_all['支付时间'])#将日期时间转换为标准形式
    data_all = data_all.set_index('支付时间')#将时间换位index格式
    #print(data_all)

    xx=input('请输入要查询 每单平均交易额 和 日均订单量 的月份。格式例：2017-05\n')

    #每单平均交易额
    data_use=data_all[xx]
    #print(data_use)
    jiao_yi_e=float(0)
    for i in range(data_use.shape[0]):#计算交易额
        jiao_yi_e=jiao_yi_e+float(data_use['实际金额'][i])
    
    zong_ding_dan_liang=data_use.shape[0]#总订单量
    mei_dan_ping_jun_jiao_yi_e=jiao_yi_e/zong_ding_dan_liang#每单平均交易额=总交易额/总订单量
    print('{name}的每单平均交易额为'.format(name=str(xx))+str('%.2f'% mei_dan_ping_jun_jiao_yi_e))#输出每单平均交易额，取小数点前两位
    #日均订单量
    if xx[-2:] in ['01','03','05','07','08','10','12']:
        tian_shu=31
    elif xx[-2:] in ['04','06','08','09','11']:
        tian_shu=31
    else:
        tian_shu=28
    ri_jun_ding_dan_liang=zong_ding_dan_liang/tian_shu
    print('{name}的日均订单量为'.format(name=str(xx))+str('%.2f'% ri_jun_ding_dan_liang))#输出日均订单量，取小数点前两位