#Caleb SMith-Salzberg
#SoftDev1 pd7
#HW4 -- Fill Up Yer Flask
#2017-09-24

from flask import Flask
app= Flask(__name__)

@app.route("/")
def hello():
    return "<b>WASSUPPPP</b>"

@app.route("/cool")
def pic1():
    return "<img src= \" https://www.cesarsway.com/sites/newcesarsway/files/styles/large_article_preview/public/Common-dog-behaviors-explained.jpg?itok=FSzwbBoi \" >"

@app.route("/cat")
def pic2():
    return "<img src= \"http://r.ddmcdn.com/s_f/o_1/cx_462/cy_245/cw_1349/ch_1349/w_720/APL/uploads/2015/06/caturday-shutterstock_149320799.jpg \" >"

if __name__ == "__main__":
    app.debug = True
    app.run()
