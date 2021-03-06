from flask import Flask
from frontend.app import frontend_bp
from backend.persistencia import Persistencia
from flask_environments import Environments

from b_logic.business import Billetera

billetera = Billetera()
persistencia = Persistencia('190.188.234.6', 'admin', 'admin2k14')
app = Flask(__name__)

env = Environments(app)
env.from_object('billetera')

app.register_blueprint(frontend_bp, url_prefix="/frontend")
#app.register_blueprint(backoffice_bp, url_prefix="/backoffice")

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)