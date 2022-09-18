from flask import Flask

def create_app():
    app = Flask(__name__)   # 플라스크 애플리케이션을 생성하는 코드야

    @app.route("/")     # url과 플라스크 코드를 매핑하는 데코레이터
    def hello_pybo():
        return "Hello, Pybo!"

    return app

#! create_app 함수가 : 애플리케이션팩토리
# 함수명 바꾸면 실행안됨 , create_app은 플라스크 내부에서 정의된 함수

