FROM python:2.7.10

ADD aa-api /opt/aa-api
RUN pip install -r /opt/aa-api/requirements.txt
CMD ["uwsgi", "--socket", ":8080", "--wsgi-file", "/opt/aa-api/api.py", "--callable", "app", "--master" ]
