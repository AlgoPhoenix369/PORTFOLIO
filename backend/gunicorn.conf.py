# Gunicorn configuration file for production deployment
import multiprocessing
import os

# Server socket
bind = os.getenv('GUNICORN_BIND', '0.0.0.0:5000')

# Worker processes
workers = os.getenv('GUNICORN_WORKERS', str(multiprocessing.cpu_count() * 2 + 1))
worker_class = 'sync'
worker_connections = 1000
threads = 2

# Worker lifecycle
max_requests = 1000
max_requests_jitter = 50
timeout = 30
keepalive = 5

# Process naming
proc_name = 'portfolio-api'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# Logging
errorlog = '-'
accesslog = '-'
loglevel = os.getenv('GUNICORN_LOG_LEVEL', 'info')
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# SSL (if needed)
# keyfile = None
# certfile = None
