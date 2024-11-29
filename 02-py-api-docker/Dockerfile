FROM python:3.12

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	PIP_DEFAULT_TIMEOUT=100 \
	PIP_NO_CACHE_DIR=1

# Install poetry
RUN python3 -m pip install pip --upgrade

# Copy files
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ctlibrary/ ./ctlibrary
COPY library/ ./library
COPY manage.py .
EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
