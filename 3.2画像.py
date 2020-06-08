import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import re
def find_chinese(file):#只保留汉字
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese
biao_ming=['task3-1A.csv','task3-1B.csv','task3-1C.csv','task3-1D.csv','task3-1E.csv']
for v in range(len(biao_ming)):
    data_all = pd.read_csv(biao_ming[v],encoding='gbk')
    #print(data_all)

    for i in range(data_all.shape[0]):#商品列中只保留汉字
        data_all['商品'][i] = find_chinese(data_all['商品'][i])
    #print (data_all)
    #提取商品和评价
    shang_pin_xiao_liang=data_all[['商品','评价']]
    print (shang_pin_xiao_liang)


    import PIL.Image as Image
    from wordcloud import WordCloud

    counts1 = {}  #创建字典，保存标签1
    for i in range(shang_pin_xiao_liang.shape[0]):
        counts1[shang_pin_xiao_liang['商品'][i]] = counts1.get(shang_pin_xiao_liang['商品'][i],0) + shang_pin_xiao_liang['评价'][i]
    items1 = list(counts1.items())   #返回所有键值对
    items1.sort(key=lambda x:x[1], reverse =True) #排序
    wordlist=list()

    for i in range(50):  #选取前50个词
        word,count = items1[i]  
        wordlist.append(word)    #把词语word放进一个列表

    wl=' '.join(wordlist)

    #图片遮罩层
    mask_pic=np.array(Image.open('1.jpg'))
    wc = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",
                            background_color="white",
                            mask=mask_pic).generate(wl)
    #显示图片
    plt.imshow(wc)
    plt.axis('off')        #关闭坐标
    plt.show()

    ming_ming=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
    wc.to_file('画像_{name}.png'.format(name=str(ming_ming[v]))) #保存