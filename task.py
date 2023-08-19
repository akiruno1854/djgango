from celery import Celery

app = Celery('tasks')
app.config_from_object('celery_config')

@app.task
def add(x, y):
    print(x+y)
    return x + y
