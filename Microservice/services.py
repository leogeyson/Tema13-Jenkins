import os

def env_vars_list():
    return os.popen('env').read()

def create_linux_env_var(env_name, env_var):
    sheelEnv = os.environ[str(env_name)] = str(env_var)
    os.popen('export '+ sheelEnv)
    return sheelEnv

def software_running_list():
    return os.popen('ps -aux').read()
