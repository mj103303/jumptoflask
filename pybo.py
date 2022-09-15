from flask import Flask

app = Flask(__name__)   # 플라스크 애플리케이션을 생성하는 코드야


@app.route("/")     # url과 플라스크 코드를 매핑하는 데코레이터
def hello_pybo():
    return "Hello, Pybo!"

