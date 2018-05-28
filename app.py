#!/usr/bin/env python3
from flask import Flask, render_template, abort
import os
import json

app = Flask(__name__) #创建app对象，传入当前程序的名字
app.config['TEMPLATES_AUTO_RELOAD'] = True #每当模板发生改变时，自动重新渲染模板

#将.json文件内容转化为字典
class Files():


    def __init__(self):
        self.files = self.read_files()

    def read_files(self): #读取文件的函数

    def get_title_list(): #获得文章名称列表函数

    def get_contents(): #获得文章内容

files = Files()

@app.route('/')
def index():
    return render_template('index.html', title_list = files.get_title_list() )

@app.route('/files/<filename>')
def file(filename):
    file_contents = files.get_contents(filename)
    if not file_contents:
        abort(404)
    return render_template('file.html', file_contents = file_contents)

@app.errorhandle(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ = '__main__':
    app.run()
