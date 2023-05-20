# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install supervisor
RUN apt-get update && apt-get install -y supervisor

# Copy supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports
EXPOSE 5000
EXPOSE 5001

# Run supervisor
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
