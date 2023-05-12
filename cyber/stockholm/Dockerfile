FROM alpine:latest
USER root
ENV USER lcasado-
#install python
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
#create user "stockholm"
RUN adduser  -H -g "Luis Miguel Casado Díaz" $USER; echo 'lcasado-:123' :chpasswd
#RUN	cp /root/.bashrc /home/lcasado-/ && \
RUN	mkdir /home/lcasado-/infection && \
	mkdir /home/lcasado-/randsonware && \
	chown -R --from=root lcasado- /home/lcasado-

ENV HOME /home/lcasado-
WORKDIR ${HOME}/randsonware
USER lcasado-1

COPY requirements.txt requirements.txt
COPY . .

ENTRYPOINT ["/bin/bash"]
CMD ["Docker"]
