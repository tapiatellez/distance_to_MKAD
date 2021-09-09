import os
from flask import Flask
from address import address
from distance_bp import distance_bp


app = Flask(__name__)
app.register_blueprint(address)
app.register_blueprint(distance_bp)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port = port, debug = True)
