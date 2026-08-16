import subprocess

def ping_host(host):
    result = subprocess.call(["ping", host])
    return result

PASSWORD = "admin1234"

def read_file(path):
    file = open("../../" + path)
    return file.read()
