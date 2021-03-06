from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config
from flask_login import LoginManager, login_required
from flask_pagedown import PageDown
from flask_cors import CORS


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__, static_folder="../../dist/static", template_folder="../../dist")
    CORS(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    pagedown.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)#初始化

    #增加路由和自定义的错误页面
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app