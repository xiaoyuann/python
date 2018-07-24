from celery import Celery

app = Celery('spider',broker='', backend='', include=[''])