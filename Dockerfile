FROM ubuntu18.04-py3.7:v1.0
WORKDIR /mnt/app
ADD . /mnt/app
RUN cd /mnt/app && pipenv sync
CMD ["/root/.local/share/virtualenvs/app-Vq3Ohy0S/bin/python","manage.py"]