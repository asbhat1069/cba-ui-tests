FROM python:3.7.0
RUN apt-get update && apt-get install --assume-yes unzip wget;apt-get --fix-broken --assume-yes install

RUN pip install -U pip


RUN wget --no-verbose https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN dpkg --install google-chrome-stable_current_amd64.deb; apt-get --fix-broken --assume-yes install

RUN CHROMEDRIVER_VERSION=`wget --no-verbose --output-document - https://chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget --no-verbose --output-document /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver && \
    chmod +x /opt/chromedriver/chromedriver && \
    ln -fs /opt/chromedriver/chromedriver /usr/local/bin/chromedriver

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /usr/src/project
ENV PYTHONPATH=.
ENV HEADLESSCHROME=true


CMD ["bash"]