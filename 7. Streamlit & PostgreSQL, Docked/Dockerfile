FROM python:3.9

WORKDIR /app

COPY main.py .
RUN pip install streamlit psycopg2

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
