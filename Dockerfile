FROM python:3.8

LABEL "repository"="https://github.com/uqmc/tibrogargan"
LABEL "homepage"="https://github.com/uqmc/tibrogargan"

WORKDIR /web
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run backend
CMD [ "python3", "./src/app.py" ]
