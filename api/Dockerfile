FROM python:3.7-slim-buster AS build

COPY ./api/setup.py /app/setup.py

WORKDIR /app
RUN python -m pip install .[seed]

FROM build AS app

COPY ./api/ /app/
COPY ./seed/Enodo_Skills_Assessment_Data_File.xlsx /data/Enodo_Skills_Assessment_Data_File.xlsx

# Create configuration
ENV SEED_DATA_PATH /data/Enodo_Skills_Assessment_Data_File.xlsx
ENV SQLITE_PATH /db/properties.db

# Migrate the database
RUN mkdir /db
RUN python api/migrate.py

ENTRYPOINT [ "python", "/app/api/app.py" ]
