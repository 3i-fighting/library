from flask_sqlalchemy import SQLAlchemy

class Config:
    # 数据库配置   mysql://用户名:密码@网址：端口/数据库名
    SQLALCHEMY_DATABASE_URI = 'mysql://root:saq20050315@127.0.0.1:3306/library'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()
