import jwt
import datetime
import uuid
from flask import Flask, jsonify
from flask_cors import CORS


#prerequisite values
connectedAppClientId = '0a9faf71-d52e-4a17-a52a-24a0d5ad694c'
connectedAppSecretId='6dac74d9-65d6-48bc-b5f7-259a23b8bd5d'
connectedAppSecretKey='2Yh9wbplndBzimew1ZZ0wU+q8k0NnKuRdnnTiyD8GSk='

#email address for TOL; username for Tableau Server
username= "m.setit@gmail.com"

#TOL or Tableau server name. SSL is highly recommeded
tableauservername ="https://10ax.online.tableau.com/t/setitsandboxdev427435/"

#JS API3.0 library
# js_api='tableau.embedding.3.0.0.min.js'

#public facing url from TOL/ Tableau server 
viz_dash_url = tableauservername + "views/CaseStudy/Q3Dashboard"


token = jwt.encode(
{
    'iss': connectedAppClientId,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
    'jti': str(uuid.uuid4()),
    'aud': 'tableau',
    'sub': username,
    'scp': ['tableau:views:embed']
    },
    connectedAppSecretKey,
    algorithm = 'HS256',
    headers = {
    'kid': connectedAppSecretId,
    'iss': connectedAppClientId
    }
)

######### 
app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/get_string')
def get_string():
    
    # Call your Python function and get the string result
    # result = your_python_function(data)

    # Return the result as JSON
    print('Here')
    return jsonify({'result': token})

if __name__ == '__main__':
    app.debug = True
    app.run()