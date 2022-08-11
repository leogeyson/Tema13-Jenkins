#!/usr/bin/python

from flask import Flask
import os
import service
app = Flask(__name__)

@app.route('/')
def home_page():
    return "Welcome to web service"
 
@app.route('/config/env')
def env_list():
   return Service.env_list()

@app.route("/env/<env_name>/<env_var>")
def create_env_var(env_name, env_var):
 return Service.create_env_var_linux(env_name, env_var)


@app.route("/list/running_software")
def running_software():
    return Service.running_software()

if __name__ == '__main__'

app.run(host='0.0.0.0',port=8080)
