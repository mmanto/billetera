# -*- coding: utf-8 -*-
from flask import render_template
from flask import request
from flask import Flask, Blueprint
from flask_environments import Environments

from frontend.views.solicitudView import SolicitudView

from backend.persistencia import Persistencia
from backend.persistencia import Util
from backend.mail_util import EMail

from b_logic.model import Solicitud


app = Flask(__name__)

env = Environments(app)
env.from_object('billetera')
frontend_bp = Blueprint('frontend', __name__,
template_folder='templates', static_folder="static")


@frontend_bp.route('/solicitud/')
def solicitud():
    return render_template('request.html')


@frontend_bp.route('/procesar-solicitud', methods=['POST', 'GET'])
def procesar_solicitud():
    
    solicitud = Solicitud(request.form)
    p = Persistencia('190.188.234.6', 'admin', 'admin2k14')
    sol = Util.asDic(solicitud)
    p.insert(sol)
    
    emailContacto = request.form['emailPagador']
    
    email = EMail('smtp.gmail.com','587')
    email.sendMailFromTemplate('prueba.mmanto@gmail.com',
                               emailContacto,
                               '',
                               'Correo de confirmación',
                               'prueba.mmanto',
                               'prueba.mmanto2k14',
                               {'title': 'Por favor seleccione el enlace para confirmar su cuenta en MisPagos',
                                'contents': 'Este es el contenido',
                                'links': [{'url' : 'www.google.com','label' : 'Ir a google...'}]},
                                'frontend/mail_templates/mail.tmpl')


    return render_template('result_request.html', d=request.form)


@frontend_bp.route('/')
def index():
    return render_template('wellcome.html')
    
'''    
@frontend_bp.route('/plans')
def plan_list(id_plan):
    return render_tempalte('plans.html')


solicitud_view=SolicitudView.as_view('solicitud_view')
frontend_bp.add_url_rule('/procesar-solicitud/',defaults={'id_plan': None},view_func=solicitud_view,methods=['GET','POST'])
frontend_bp.add_url_rule('/procesar-solicitud/<solicitud>',view_func=solicitud_view,methods=['GET'])


plan_view=PlanView.as_view('plan_view')
frontend_bp.add_url_rule('/plans/',defaults={'id_plan': None},view_func=plan_view,methods=['GET','POST'])
frontend_bp.add_url_rule('/plans/<id_plan>',view_func=plan_view,methods=['GET'])



if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
'''


