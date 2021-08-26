FROM python:3.9-alpine3.12
COPY ./ /app
RUN pip install -r app/requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
