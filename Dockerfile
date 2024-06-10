FROM python:3.10-slim-bookworm

WORKDIR /streamlit-docker

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "streamlit", "run", "myfirstapp.py",  "--server.port=8501", "--server.address=0.0.0.0"]