from flask import Flask,request,render_template,flash

app = Flask(__name__)

@app.route('/', method=['GET','POST'])
def index():
	return render_template(index.html)
	if method.type == 'POST':
		

if __name__ == '__main__ ':
	app.run(debug=True)