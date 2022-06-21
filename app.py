from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    #return "Starting Machine Learning Project"
    return 'CICD pipelines are created'

if __name__ =='__main__':
    app.run(debug=True)