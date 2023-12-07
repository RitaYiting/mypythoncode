# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 23:17:28 2023

@author: User
"""

from flask import Flask,render_template,request,redirect,url_for
from flask_paginate import Pagination,get_page_parameter;
from ctarateBank import Bankrates


app = Flask(__name__)

@app.route("/ctabank")

def CTARate():

    rates = Bankrates()

    
    return render_template('ctabank.html', **locals())



app.run()