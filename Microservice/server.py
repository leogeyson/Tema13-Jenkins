#!/usr/bin/python

from flask import Flask
import os
import services
app = Flask(__name__)

@app.route("/serverstatus")
def serverstatus():
    return "Server is good"

@app.route("/")
def home_page():
    return "Welcome to python web service test<br>All available urls:<br>~/serverstatus (to check if the server is working)<br>~/conf/env (list all linux environment variables)<br>~/softrun (list of all running softwares (PID and cmd)<br>~/env/any entry/any entry (create a linux env_var)"

@app.route("/conf/env")
def env_vars_list():
    return services.env_vars_list()

@app.route("/env/<env_name>/<env_var>")
def create_linux_env_var(env_name, env_var):
    return services.create_linux_env_var(env_name, env_var)

@app.route("/softrun")
def software_running_list():
    return services.software_running_list()

if __name__ == '__main__':
    app.run(port=8282, debug=True, host="0.0.0.0")
