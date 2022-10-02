FROM python:3.8
WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY stock.jpeg final_version/project/stock.jpeg
COPY s&p500.csv final_version/project/s&p500.csv
RUN pip3 install -r requirements.txt
EXPOSE 8501
COPY . /app
ENTRYPOINT [ "streamlit", "run" ]
CMD ["final_project.py"]