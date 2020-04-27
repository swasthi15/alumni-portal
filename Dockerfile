FROM python:3.7

RUN mkdir /code
WORKDIR /code
ADD $PWD/requirements.txt /code/
RUN pip install -r requirements.txt
ADD $PWD /code/


EXPOSE 8000 2222
CMD ["python", "/code/manage.py", "runserver", "0.0.0.0:8000"]
