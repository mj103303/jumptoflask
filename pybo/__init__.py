from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config   # 이렇게 임포트를 하네

db = SQLAlchemy()   # 전역변수
migrate = Migrate() # 전역변수



def create_app():
    app = Flask(__name__, )   # 플라스크 애플리케이션을 생성하는 코드야
    app.config.from_object(config)
      

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models  
    
    # blueprint    
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    

    return app

#! create_app 함수가 : 애플리케이션팩토리
# 함수명 바꾸면 실행안됨 , create_app은 플라스크 내부에서 정의된 함수

