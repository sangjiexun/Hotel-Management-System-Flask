from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, TimeField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from datetime import datetime
import os

# 初始化Flask应用
app = Flask(__name__)
app.config.from_object('config')

# 初始化数据库
db = SQLAlchemy(app)

# 初始化登录管理器
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# 导入模型
from app.models import User, Team, Room, Meeting, CostLog, Participants_user, Participants_partner, Businesspartner

# 导入表单
from app.forms import LoginForm, RegistrationForm, RoomForm, MeetingForm, TeamForm

# 导入路由
from app.routes import *

# 登录管理器回调
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 主函数
if __name__ == '__main__':
    # 创建数据库表
    with app.app_context():
        db.create_all()
        
        # 创建管理员用户（如果不存在）
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', email='admin@example.com', password='admin123', role='admin')
            db.session.add(admin)
            db.session.commit()
        
        # 创建示例团队（如果不存在）
        if not Team.query.first():
            teams = [
                Team(name='Management Team', description='Company management team'),
                Team(name='Technical Team', description='Technical department team'),
                Team(name='Marketing Team', description='Marketing department team')
            ]
            for team in teams:
                db.session.add(team)
            db.session.commit()
        
        # 创建示例房间（如果不存在）
        if not Room.query.first():
            rooms = [
                Room(name='Conference Room A', capacity=20, equipment='Projector, Whiteboard'),
                Room(name='Conference Room B', capacity=10, equipment='Whiteboard'),
                Room(name='Meeting Room 1', capacity=8, equipment='TV'),
                Room(name='Meeting Room 2', capacity=6, equipment='Whiteboard')
            ]
            for room in rooms:
                db.session.add(room)
            db.session.commit()
    
    app.run(debug=True)