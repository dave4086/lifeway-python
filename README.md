## lifeway-python

Local Testing Notes:

Docker build command :
```
docker build -f Dockerfile -t lifeway-python:latest .
```
Docker run command :
```
docker run -p 5000:5000 lifeway-python
```

After app is running, POST to http://localhost:5000/api/messages with JSON body like below.

{
    "id": "2",
    "message": "test test test"
}

If that ID doesn't exist, it should write to the database and return a count of words in the message field.
If the ID does exist, it should return a warning about that ID already existing.




#### Tech

Used the following Python libraries

- [sqlAlchemy]
- [Flask-restful]
- [Flask-Marshmallow]

## To-Do/Improvement Opportunities

