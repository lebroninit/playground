from flask import Flask, render_template
app = Flask(__name__)                     
    
@app.route('/')                           
def hello_world():
    return render_template('index.html', color = "DarkTurquoise", times=3)  
    
@app.route('/play/<x>')                           
def hello_world2(x):
    return render_template('index.html', color = "DarkTurquoise", times=int(x))  

@app.route('/play/<x>/<colors>')                           
def hello_world3(x,colors):
    return render_template('index.html', color = colors, times=int(x))  


if __name__=="__main__":
    app.run(debug=True)    