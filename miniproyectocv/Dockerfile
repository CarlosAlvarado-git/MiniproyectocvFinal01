FROM python:3.8
ENV PROJECT_ROOT=/srv
WORKDIR $PROJECT_ROOT

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "CV.py"]

EXPOSE 5000:5000