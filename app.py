from ast import Global
from fileinput import filename
from operator import index
from flask import Flask, flash, redirect,render_template, request, session, abort, send_from_directory
from zipfile import ZipFile
from rarfile import RarFile
import rarfile
import wget
from os import walk
import urllib
import shutil
import seedir as sd

rarfile.UNRAR_TOOL ='unrar'
# from flask_sqlalchemy import SQLAlchemy
# import magic
# import enum
import os
# app = Flask(__name__,static_folder='savedir')
app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///files.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
# db = SQLAlchemy(app)

# class Files(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     fname=db.Column(db.String(200), nullable=False)
#     fsize=db.Column(db.String(500), nullable=False)
#     fcsize=db.Column(db.String(500), nullable=False)

#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.fname}"

@app.route('/', methods=['GET', 'POST'])
def Homein():
    return render_template("index.html")

@app.route('/Homeins', methods=['GET', 'POST'])
def Homeins():
    if request.method =='POST':
      if os.path.exists('savedir'):
        shutil.rmtree('savedir')
      # db.session.query(Files).delete()
      # db.session.commit()
      nfile= request.files['nfile']
      blob = request.files['nfile'].read()
      global fsize
      fsize = len(blob)
      fsize=f'{fsize / 1000} kb'
      global file
      with RarFile(nfile) as file:
        file.extractall("savedir")
      global files
      files =file.namelist()
      index=0
      global nlfile
      nlfile=files[0].split('/')
      global nfiles
      nfiles=os.listdir(f'savedir/{nlfile[0]}')
      res=[]
      for filee in os.listdir(f'savedir/{nlfile[0]}'):
          if os.path.isfile(f'savedir/{nlfile[0]}/{filee}'):
            res.append(filee)
      global dictf
      dictf={}
      dictf[nlfile[0]]=res
      for fil in nfiles:
        if f"{nlfile[0]}/" == fil:
          files.remove(fil)
        index +=1
      for filee in nfiles:
        if os.path.isfile(f'savedir/{nlfile[0]}/{filee}') == True:
          fileinfo=file.getinfo(f'{nlfile[0]}/{filee}')
          filesize=f'{fileinfo.file_size / 1000} kb'
          filecsize=f'{fileinfo.compress_size / 1000} kb'
        elif os.path.isdir(f'savedir/{nlfile[0]}/{filee}') == True:
          global filenames
          filenames=os.listdir(f'savedir/{nlfile[0]}/{filee}')
          dictf[filee]=filenames
    nelfile=nlfile[0].title()
    return render_template("home.html",size=fsize,dicti=dictf,hhhname=nelfile)

@app.route('/download/<foln>/<ffname>', methods=['GET', 'POST'])
def download(foln,ffname):
  for file in nfiles:
    if ffname in file:
      return send_from_directory(directory=f'savedir/{foln}', path=file, as_attachment=True)
  for files in filenames:
    if ffname in files:
      return send_from_directory(directory=f'savedir/{nlfile[0]}/{foln}',path=files, as_attachment=True)
  return render_template("home.html",dicti=dictf,size=fsize)

@app.route('/downloadall', methods=['GET', 'POST'])
def downloadall():
  for file in nfiles:
    sendfile=shutil.make_archive(f'savedir/{nlfile[0]}', 'zip', f'savedir/{nlfile[0]}')
    return send_from_directory(directory='savedir', path=f'{nlfile[0]}.zip', as_attachment=True)
  return render_template("home.html",dicti=dictf,size=fsize)


@app.route('/reading/<path:filename>', methods=['GET', 'POST'])
def reading(filename):
  for file in nfiles:
    if filename in file:
      f=open(f'savedir/{file}','r')
      content_list = [line.rstrip() for line in f]
  filename=filename.title()
  # alllib = Files.query.all()
  return render_template("home.html",size=fsize,hname=filename,content=content_list)

if __name__ == "__main__":
  app.run(debug=True)