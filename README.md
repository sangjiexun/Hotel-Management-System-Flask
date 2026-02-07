# 酒店管理系统

## 项目简介
酒店管理系统是一个基于Flask框架开发的酒店运营管理平台，提供房间预订、会议管理、团队管理和成本核算等功能，帮助酒店提高运营效率和管理水平。

## 技术架构

### 后端技术
- **Flask**: Python Web框架
- **Flask-SQLAlchemy**: ORM数据库工具
- **Flask-Login**: 用户认证管理
- **Flask-WTF**: 表单处理和验证
- **SQLite**: 轻量级数据库

### 前端技术
- **HTML5/CSS3/JavaScript**: 前端基础
- **Jinja2**: 模板引擎
- **Bootstrap**: 响应式UI框架

### 项目结构
```
Hotel-Management-System/
├── lab2.py               # 主应用文件
├── config.py             # 配置文件
├── app/
│   ├── __init__.py       # 应用初始化
│   ├── models.py         # 数据库模型
│   ├── forms.py          # 表单定义
│   └── routes.py         # 路由定义
└── templates/
    ├── base.html         # 基础布局
    ├── index.html        # 首页
    ├── login.html        # 登录页面
    ├── register.html     # 注册页面
    ├── book.html         # 预订页面
    ├── roomavailable.html # 房间可用查询
    ├── roomavailablelist.html # 房间可用列表
    ├── roomoccupation.html # 房间占用查询
    ├── roomoccupationlist.html # 房间占用列表
    ├── costs.html        # 成本页面
    ├── costcheck.html    # 成本查询
    └── allrecords.html   # 所有记录
```

## 核心功能

### 用户管理
- 用户注册与登录
- 权限控制

### 房间管理
- 房间类型管理
- 房间状态查询
- 房间预订管理

### 会议管理
- 会议预订
- 会议参与者管理
- 会议资源分配

### 团队管理
- 团队信息管理
- 团队成员管理

### 成本管理
- 成本记录
- 成本查询与统计
- 成本分析

### 业务伙伴管理
- 业务伙伴信息管理
- 合作记录

## 数据库模型

### 主要模型
- **User**: 用户信息
- **Team**: 团队信息
- **Room**: 房间信息
- **Meeting**: 会议信息
- **CostLog**: 成本记录
- **Participants_user**: 用户参与者
- **Participants_partner**: 伙伴参与者
- **Businesspartner**: 业务伙伴

## 安装与运行

### 环境要求
- Python 3.6+
- pip包管理器

### 安装步骤
1. 克隆仓库
   ```bash
   git clone https://github.com/sangjiexun/Hotel-Management-System-Flask.git
   cd Hotel-Management-System-Flask
   ```

2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

3. 运行应用
   ```bash
   python lab2.py
   ```

4. 访问应用
   打开浏览器访问 http://localhost:5000

## 配置说明

### 数据库配置
默认使用SQLite数据库，可在`config.py`中修改：

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///hotel.db'
```

### 应用配置
```python
SECRET_KEY = 'your-secret-key'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## 安全措施
- 密码哈希存储
- CSRF保护
- 权限控制
- 输入验证

## 部署建议
- 使用Gunicorn作为WSGI服务器
- 使用Nginx作为反向代理
- 配置HTTPS
- 数据库定期备份

## 贡献指南
欢迎提交Issue和Pull Request来改进这个项目。

## 许可证
MIT License

---

# Hotel Management System

## Project Introduction
Hotel Management System is a hotel operation management platform developed based on the Flask framework, providing room reservation, meeting management, team management, and cost accounting functions to help hotels improve operational efficiency and management level.

## Technical Architecture

### Backend Technology
- **Flask**: Python Web framework
- **Flask-SQLAlchemy**: ORM database tool
- **Flask-Login**: User authentication management
- **Flask-WTF**: Form handling and validation
- **SQLite**: Lightweight database

### Frontend Technology
- **HTML5/CSS3/JavaScript**: Frontend basics
- **Jinja2**: Template engine
- **Bootstrap**: Responsive UI framework

### Project Structure
```
Hotel-Management-System/
├── lab2.py               # Main application file
├── config.py             # Configuration file
├── app/
│   ├── __init__.py       # Application initialization
│   ├── models.py         # Database models
│   ├── forms.py          # Form definitions
│   └── routes.py         # Route definitions
└── templates/
    ├── base.html         # Base layout
    ├── index.html        # Home page
    ├── login.html        # Login page
    ├── register.html     # Registration page
    ├── book.html         # Reservation page
    ├── roomavailable.html # Room availability query
    ├── roomavailablelist.html # Room availability list
    ├── roomoccupation.html # Room occupancy query
    ├── roomoccupationlist.html # Room occupancy list
    ├── costs.html        # Cost page
    ├── costcheck.html    # Cost query
    └── allrecords.html   # All records
```

## Core Features

### User Management
- User registration and login
- Permission control

### Room Management
- Room type management
- Room status query
- Room reservation management

### Meeting Management
- Meeting reservation
- Meeting participant management
- Meeting resource allocation

### Team Management
- Team information management
- Team member management

### Cost Management
- Cost recording
- Cost query and statistics
- Cost analysis

### Business Partner Management
- Business partner information management
- Cooperation records

## Database Models

### Main Models
- **User**: User information
- **Team**: Team information
- **Room**: Room information
- **Meeting**: Meeting information
- **CostLog**: Cost records
- **Participants_user**: User participants
- **Participants_partner**: Partner participants
- **Businesspartner**: Business partners

## Installation and Running

### Environment Requirements
- Python 3.6+
- pip package manager

### Installation Steps
1. Clone the repository
   ```bash
   git clone https://github.com/sangjiexun/Hotel-Management-System-Flask.git
   cd Hotel-Management-System-Flask
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application
   ```bash
   python lab2.py
   ```

4. Access the application
   Open a browser and visit http://localhost:5000

## Configuration Instructions

### Database Configuration
SQLite is used by default, which can be changed in `config.py`:

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///hotel.db'
```

### Application Configuration
```python
SECRET_KEY = 'your-secret-key'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## Security Measures
- Password hash storage
- CSRF protection
- Permission control
- Input validation

## Deployment Recommendations
- Use Gunicorn as WSGI server
- Use Nginx as reverse proxy
- Configure HTTPS
- Regular database backups

## Contribution Guide
Welcome to submit Issues and Pull Requests to improve this project.

## License
MIT License