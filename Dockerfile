 00 but once I hey let me call you right back let me call you right back my roommate just walked in my room really quick i'll be back take a bath what's it look like oh really oh no no worries and what's up Mike FaceTime Snow Rush flag yeah well yeah text I like Will you get your hair yeah yeah I saw my and she was in a map House it was light glasses no location so I don't know find what i'll check in there yeah chopstix Close is this I think it's called what are you doing oh I need that another they still have it like i'll go to we can because I'm like yo this weekend room pops up to the weekly routine sleep it's cool yeah back in the day I mean who is this 60s ball out of my demons give me that I love like technology yeah people Contacts yeah yeah yeah we all# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "balance.py"]
