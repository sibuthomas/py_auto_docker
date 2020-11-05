FROM python:3.8.3-buster

LABEL version="1.0"
LABEL description="FZ Container example" 

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get -y install google-chrome-stable xvfb \
    && useradd -rm -d /home/seluser -s /bin/bash -g root -G sudo -u 1001 seluser

WORKDIR /home/seluser/fz_auto

COPY requirements.txt ./
COPY *.py ./
COPY pytest.ini ./

RUN chown -R seluser:root ../fz_auto 

USER seluser
ENV PATH="${PATH}:/home/seluser/.local/bin"

RUN pip install --user -r requirements.txt
#CMD ["xvfb-run", "-a","pytest","fz_home_page_test.py"]