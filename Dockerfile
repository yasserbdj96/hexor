# docker build -t hexor-docker .
# docker run -i -t hexor-docker
# 
FROM python:3.9

WORKDIR /wrdir

COPY ./examples.py /wrdir
COPY ./hexor /wrdir/hexor

CMD ["python", "examples.py"]