FROM python:3.11-slim

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile","Pipfile.lock","./"]

# RUN pipenv install --system --deploy
RUN pipenv install --deploy --ignore-pipfile
RUN pipenv install Jinja2
RUN pipenv install flask

COPY ["predict.py","./"]

EXPOSE 9696

ENTRYPOINT [ "pipenv", "run", "waitress-serve","--listen=0.0.0.0:9696", "predict:app" ]
# CMD ["waitress-serve", "--port=9696", "predict:app"]
# CMD ["pipenv", "run", "waitress-serve", "--port=9696", "predict:app"]