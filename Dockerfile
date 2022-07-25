#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

######## local build & run:
# docker build -t hexor:latest .
# docker run -e T="hex" -e TEXT="Text is red" -e FC="#ff0000" -i -t hexor:latest
# docker run -e T="hex" -e TEXT="Text is red and background is blue" -e FC="#ff0000" -e BG="1a73e8" -i -t hexor:latest

######## docker.io pull, build & run:
# docker pull docker.io/yasserbdj96/hexor:latest
# docker build -t docker.io/yasserbdj96/hexor:latest .
# docker run -e T="hex" -e TEXT="Text is red" -e FC="#ff0000" -i -t docker.io/yasserbdj96/hexor:latest
# docker run -e T="hex" -e TEXT="Text is red and background is blue" -e FC="#ff0000" -e BG="1a73e8" -i -t docker.io/yasserbdj96/hexor:latest

######## ghcr.io pull, build & run:
# docker pull ghcr.io/yasserbdj96/hexor:latest
# docker build -t ghcr.io/yasserbdj96/hexor:latest .
# docker run -e T="hex" -e TEXT="Text is red" -e FC="#ff0000" -i -t ghcr.io/yasserbdj96/hexor:latest
# docker run -e T="hex" -e TEXT="Text is red and background is blue" -e FC="#ff0000" -e BG="1a73e8" -i -t ghcr.io/yasserbdj96/hexor:latest

#START{
FROM python:3.10

WORKDIR /wrdir

COPY ./run.py /wrdir
COPY ./hexor /wrdir/hexor

CMD ["python", "run.py"]
#}END.