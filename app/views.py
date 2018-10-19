#encoding=utf8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import commands
import flask 
from app import app 
from flask import render_template,request,url_for
#from app.forms import LoginForm,RegistForm
from werkzeug import secure_filename

@app.route('/upload',methods=('GET','POST'))
def upload():
    if request.method == 'POST':
        #print '\n'.join(['%s:%s' % item for item in request.__dict__.items()])
        try:
            starttime=time.time()
            f = request.files['filename']
            upload_path=os.path.join('/data/flask_data',secure_filename(f.filename))
            f.save(upload_path)
            endtime=time.time()
            real_time=float('%0.2f' % (endtime-starttime))
            command="du -sh /data/flask_data/"+f.filename+"| awk '{print $1}'"
            file_size=commands.getoutput(command)
            result='文件"'+f.filename+'"上传成功'
            #f.save(os.path.join(app.config['file_path'],'/',secure_filename(f.filename))
            #return redirect(url_for('upload'))
            return render_template('upload_file.html',result=result,file_size='文件大小：'+file_size,time='上传耗时：'+str(real_time)+'s')
        except Exception,e:
            result="文件上传失败："+str(e)
            return render_template('upload_file.html', result=result)
    else:
        return render_template('upload_file.html',result='')
