'''
Created on 16/02/2013

@author: leonardoleenen
'''

from flask.views import MethodView
from flask import render_template,request,session,flash
from b_logic.model import Solicitud


class SolicitudView(MethodView):
    
    def get(self,id_plan):
        #return render_template("result_request.html",plan=p,commerce=c.name,taxId=c.taxId,email=c.email)
        return "ingreso por get!"
    
    def post(self,id_plan):
        solicitud = Solicitud(request.form);
        
        '''
        p=plan.get(request.form["id_plan"])
        p.subscribe_with_bankAccount(session["signature"], 
                                     request.form["customerDescription"], 
                                     request.form["email"], 
                                     request.form["bankAccount"], 
                                     request.form["periods"])
                                     request.form["periods"])
        '''                          
        flash("mensaje")
        
        return render_template('result_request.html', solicitud=solicitud)

