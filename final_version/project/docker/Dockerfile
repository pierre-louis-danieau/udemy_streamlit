FROM python:3.8
WORKDIR /app
COPY requirements_project.txt ./requirements_project.txt
RUN pip3 install -r requirements_project.txt
EXPOSE 8501
COPY . /app
ENTRYPOINT [ "streamlit", "run" ]
CMD ["final_project.py"]