###
# Docker for Streamlit app
#
# Author: Álvaro Ferreira Pires de Paiva (alvarofepipa@gmail.com)
#
# Inspired by https://towardsdatascience.com/how-to-deploy-a-semantic-search-engine-with-streamlit-and-docker-on-aws-elastic-beanstalk-42ddce0422f3
#
FROM python:3.8-slim-buster

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV STREAMLIT_PORT 8501

EXPOSE $STREAMLIT_PORT

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]
