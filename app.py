#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def fhuh():
    return render_template('add.html')
@app.route('/infor',methods=['GET','POST'])
def hutf():
    if(request.method=='POST'):
        o=int(request.form['one'])
        t=int(request.form['two'])
        total=o+t
        return render_template('add.html',shubham=total)
if __name__=='__main__':
    app.run()

