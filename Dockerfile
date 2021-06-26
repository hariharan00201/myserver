# init a base image (Alpine is small Linux distro)
FROM python:3.8.5-slim-buster
# define the present working directory
WORKDIR /app
# copy the contents into the working dir
ADD  requirements.txt /app
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /app
CMD ["python","server.py"]
CMD ["python","session_server.py"]
