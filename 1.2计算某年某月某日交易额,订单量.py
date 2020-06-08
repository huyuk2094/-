import pandas as pd

#计算某年某月某日交易额,订单量
biao_ming=['task1-1A.csv','task1-1B.csv','task1-1C.csv','task1-1D.csv','task1-1E.csv']
for i in range(len(biao_ming)):
    wen_jian_ming=biao_ming[i]
    print('现在进行的是对'+str(wen_jian_ming)+'的操作')
    data_all = pd.read_csv(wen_jian_ming,encoding='gbk')
    #print(data_all)

    data_all['支付时间'] = pd.to_datetime(data_all['支付时间'])#将日期时间转换为标准形式
    data_all = data_all.set_index('支付时间')#将时间换位index格式
    #print(data_all)

    #计算末某年某月某日交易额,订单量
    xx=input('请输入要查询交易总额和订单总量的年份或月份或日期。格式例：2017-05-02或2017-05或2017或all\n')
    if xx=='all':
        data_use=data_all
        jiao_yi_e=float(0)
        for i in range(data_use.shape[0]):#计算交易额
            jiao_yi_e=jiao_yi_e+float(data_use['实际金额'][i])
        print('所有订单的交易总额为'+str('%.2f'% jiao_yi_e))#输出所得交易总额，取小数点前两位
        ding_dan_liang=data_use.shape[0]
        print('所有订单的订单总量为'+str(ding_dan_liang))#输出所得订单量

    else:
        data_use=data_all[xx]
        #print(data_use)
        jiao_yi_e=float(0)
        for i in range(data_use.shape[0]):#计算交易额
            jiao_yi_e=jiao_yi_e+float(data_use['实际金额'][i])
        print('{name}的交易总额为'.format(name=str(xx))+str('%.2f'% jiao_yi_e))#输出所得交易总额，取小数点前两位
        ding_dan_liang=data_use.shape[0]
        print('{name}的订单总量为'.format(name=str(xx))+str(ding_dan_liang))#输出所得订单量