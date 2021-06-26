## lifeway-python

Local Testing Notes:

Docker build command : docker build -f Dockerfile -t lifeway-python:latest .
Docker run command : docker run -p 5001:5000 lifeway-python

After app is running, POST to http://localhost:5001/api/messages with JSON body like below.

{
    "id": "2",
    "message": "test test test"
}

If that ID doesn't exist, it should write to the database and return a count of words in the message field.
If the ID does exist, it should return a warning about that ID already existing.


# To-do
- Add tests and see about CircleCI build
- Configure AWS deployment pipeline
- Refactor some sloppy code
