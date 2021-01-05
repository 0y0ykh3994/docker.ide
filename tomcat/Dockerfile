FROM tomcat:latest

ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH

RUN mkdir -p /source/webapp/

COPY tomcat-user.xml "$CATALINA_HOME"/conf/
COPY context.xml "$CATALINA_HOME"/conf/
COPY server.xml "$CATALINA_HOME"/conf/

EXPOSE 8080

CMD ["catalina.sh", "run"]