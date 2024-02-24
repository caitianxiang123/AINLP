from flask import jsonify # 从flask框架中导入jsonify函数，用于将数据转换为JS0N格式的响应
from flask import request # 从flask框架中导入request对象，用于获取客户端发送的请求数据。
import json # 导入json模块，用于处理JSON数据
from flask import Flask # 从flask框架中导入Flask类，用于创建Web应用。
app = Flask(__name__) # 创建一个Flask应用实例。


def get_word(word): # 定义一个函数，接受一个单词作为参数，目前函数体仅返回接收到的单词。
    return word # {}


@app.route("/nlp/words", methods=["GET", "POST"]) # 使用app.route装饰器定义路由，指定URL路径和接受的请求方法
def nlp_service(): # 定义处理该路由请求的函数
    data = request.get_data() # 从请求中获取数据
    result_data = json.loads(data) # 将获取到的数据从JS0N格式解析为Python字典。
    # value = result_data.get("result", "")
    # return jsonify({"code": 200, "result": value})
    word = result_data.get("word", "") # 从解析后的数据中获取键为"word"的值，如果不存在则默认为空字符串
    value = get_word(word) # 调用get_word函数处理获取到的单词
    return jsonify({"code": 200, "result": value}) # 使用jsonify函数构建JS0N格式的响应，包含状态码和处理结果.


if __name__ == "__main__": # #判断是否为主程序运行，而非模块导入。
    app.run(host='0.0.0.0', port=50001) # 启动Flask应用，指定监听的主机地址和端口号。
