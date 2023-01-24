import os, sys

sys.path.append('/home/v/vjnautils/.local/lib/python3.8/site-packages') 
sys.path.append('/home/v/vjnautils/todo/public_html')


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djsite.settings")

application = get_wsgi_application()