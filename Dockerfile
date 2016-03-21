FROM python:2.7.10

ADD api /opt/api
RUN pip install -r /opt/api/requirements.txt
CMD ["uwsgi", "--socket", ":8080", "--wsgi-file", "/opt/api/api.py", "--callable", "app", "--master" ]
