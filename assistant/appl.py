import os

def open_application(application):
    os.system(f'start {application}')


def close_application(application):
     os.system(f'taskkill /F /IM {application}.exe')