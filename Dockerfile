FROM python:3.9-slim

WORKDIR /EcoSort

COPY . .

# Install dependencies
RUN pip install flask
RUN pip install numpy
RUN pip install Pillow
RUN pip install flask_cors
RUN pip install tensorflow

# Expose port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
