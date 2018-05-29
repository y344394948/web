#!/usr/bin/env python3
from flask import Flask, render_template, abort
import os
import json

app = Flask(__name__) #创建app对象，传入当前程序的名字
app.config['TEMPLATES_AUTO_RELOAD'] = True #每当模板发生改变时，自动重新渲染模板

#将.json文件内容转化为字典
class Files():

    directory = os.path.join(os.path.abspath(os.path.dirname(__name__)), '..', 'files')

    def __init__(self):
        self.files = self.read_files()

    def read_files(self): #读取文件的函数
        result = {}
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            with open(file_path) as f:
                result[filename[:-5]] = json.load(f)
        return result
    def get_title_list(self): #获得文章名称列表函数
        return [item['title'] for item in self.files.values()]
    def get_by_filename(self, filename): #获得文章内容
        return self.files.get(filename)


files = Files()

@app.route('/')
def index():
    return render_template('index.html', title_list = files.get_title_list() )

@app.route('/files/<filename>')
def file(filename):
    file_item = files.get_by_filename(filename)
    if not file_item:
        abort(404)
    return render_template('file.html', file_item=file_item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
