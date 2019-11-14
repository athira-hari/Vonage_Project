FROM ubuntu
ADD ./Dockerscript.sh
RUN chmod +x Dockerscript.sh
CMD [ "./Dockerscript.sh" ]