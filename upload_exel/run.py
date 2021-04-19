from flask import Flask, request, make_response, session, render_template, redirect, url_for
import pandas as pd
# 导入matplotlib库的pyplot模块
from matplotlib import pyplot as plt


# 设置中文字体
plt.rcParams['font.serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

visual_dict= {'分布': {'data':['Bar','Line','Scatter'],'relation':['Map','Path']},'组成':{'data':['Pie','Radar','Sunburst'],'relation':['Tree']},'比较':['Bar','Line','Scatter'],'关联':['Relation']}

class DataStore():
    path = None
data = DataStore()

app = Flask(__name__)
app.config["SECRET_KEY"] = 'a040d6602e25484380379fed3090bff2'

@app.route('/')     #渲染主页
def index():
    return render_template('index.html')

@app.route('/upload_success',methods=['GET','POST'])
def upload_success():
    if request.method == 'POST':  # 请求方式只能为post
        file = request.files.get('f')  # 定义file对象，上传名为f的文件
        file.save(file.filename)  # 保存在本地，保存名称为原文件名
        path = '/Users/szh/PycharmProjects/my_flaskProject/' + file.filename
        data.path = path
        df = pd.read_excel(data.path)
        head_row = df.columns.values
        return render_template('success.html', filename=file.filename, head_row=head_row)

@app.route('/choose',methods=['POST'])
def choose():
    s1 = request.form['s1']
    s2 = request.form['s2']
    s3 = request.form['s3']
    df = pd.read_excel(data.path,usecols=[s1,s2,s3])
    print(df)
    # df.index = df[s1].tolist()
    # print(df)
    # df.plot(kind='line', title='感兴趣数据的统计图')
    df.plot(x=s1,y=s2, title='感兴趣数据的统计图')
    plt.show()
    df.plot(x=s1, y=s3, title='感兴趣数据的统计图')
    plt.show()
    df.plot(x=s1, y=[s2,s3], title='感兴趣数据的统计图')
    plt.show()

    return render_template('choose.html',s1=s1,s2=s2,s3=s3)

if __name__ == '__main__':
    app.run(debug=True)
