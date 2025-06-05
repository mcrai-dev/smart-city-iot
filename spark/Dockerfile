# spark/Dockerfile
FROM bitnami/spark:latest
COPY process.py /opt/process.py
CMD ["spark-submit", "/opt/process.py"]
