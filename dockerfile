FROM python:3.10.5

WORKDIR /app

# copying everything to /app
COPY . .

RUN pip install -r requirements.txt
# to run both celery and the gunicorn
# RUN chmod +x entrypoint.sh
# ENTRYPOINT [ "./entrypoint.sh" ]
CMD ["gunicorn", "--bind", "0.0.0.0:5000","app:app"]