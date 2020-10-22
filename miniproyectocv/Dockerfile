FROM python:3.8
ENV PROJECT_ROOT=/srv
WORKDIR $PROJECT_ROOT

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000:5000
CMD ["python", "CV.py"]

