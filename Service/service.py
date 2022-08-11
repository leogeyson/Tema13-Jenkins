import os

def env_list():
    return os.popen('env').read()

def create_env_var_linux(env_name, env_var):
    var = os.environ[str(env_name)] = str(env_var)
    os.popen('export '+ var)
    return var

def running_list():
    return os.popen('ps aux').read()
