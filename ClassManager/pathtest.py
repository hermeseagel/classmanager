import os.path
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static")
MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static","media")
print(STATIC_ROOT)
print('BASE',BASE_DIR)
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)
static=os.path.join(os.path.dirname(__file__), '..', 'static').replace('\\','/')
print(TEMPLATE_DIRS)
print(static)