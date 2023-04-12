FROM --platform=linux/x86-64 python:3.9

WORKDIR app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY  . .

# allow access to .sh filef
# RUN ["chmod", "+x", "/usr/src/app/deploy.sh"]

# run entrypoint.prod.sh
# ENTRYPOINT ["/usr/src/app/deploy.sh"]

# Expose port
EXPOSE 8000

CMD ["uvicorn", "app:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
