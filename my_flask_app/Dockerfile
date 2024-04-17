FROM python:3
WORKDIR /home/markus/scripst/docFlas/my_flask_app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]