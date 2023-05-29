from flask import Flask
from flask import request
import sys
# sys.path.append('./')
# sys.path.append('../')
# import gpt
import openai
openai.api_key = "{your api key}"
def chat_with_gpt(prompt,model):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
    #         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    #         {"role": "user", "content": "Where was it played?"}
        ]
    )
    return completion.choices[0].message
def chat_with_gpt2(prompt,model):
#     print(numpy.__version__)
#     return numpy.__version__
        response = openai.Completion.create(
        engine=model,# 使用高级引擎，但也可以选择其他引擎
        prompt=prompt,
        max_tokens=50,# 最大响应长度
        n=1,# 返回1
        stop=None,# 响应结束标志（如设置为["\n"]）
        temperature=0.8,# 决定输出随机性的温度参数
        top_p=1,# 对结果进行限制的累积概率（值在0和1之间）
        )
        message = response.choices[0].text.strip()
        return message
app = Flask(__name__)
def Image_with_gpt(prompt,size):
    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size=size
)
    image_url = response['data'][0]['url']
    return image_url

@app.route('/getImage')
def get_Image():
    prompt=request.args.get('prompt', 'cat')
    size=request.args.get('size', '1024x1024')
    return Image_with_gpt(prompt,size)
    
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getMes')
def get_Mes():
    print(sys.path)
    msg=request.args.get('msg', '')
    model=request.args.get('model','gpt-3.5-turbo')
    if model=='gpt-3.5-turbo':
        return {"ans":chat_with_gpt(msg,model)}
    else :
        return {"ans":chat_with_gpt2(msg,model)}
# @app.route('/')
# def hello_world():
#     return 'Hello World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0")