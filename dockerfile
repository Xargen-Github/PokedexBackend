FROM python
WORKDIR /home
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt