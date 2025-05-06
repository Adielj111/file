from flask import Flask,render_template,url_for,request
import random
import pandas as pd

app= Flask(__name__)

@app.route('/hm',methods=['GET'])
def pick(number):
    if request.method=="GET":
        number=request.get['number']
    random.seed(number)
    win=random.choice(names)
    return(win)

names =["Adiel","Jake","John","Derin"]
number=int(input("Enter a number:"))

#value = pick(number)
print(pick(number))

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)


