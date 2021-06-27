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

To test the AWS deployment the following POSTMAN tests should suffice.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/16387030-9364dab5-d6bb-491c-b766-1a71856b8117?action=collection%2Ffork&collection-url=entityId%3D16387030-9364dab5-d6bb-491c-b766-1a71856b8117%26entityType%3Dcollection%26workspaceId%3D81a6d3be-b965-44ff-a577-4f7cb4f56f09)




#### Tech

Used the following Python libraries

- [sqlAlchemy](https://www.sqlalchemy.org/)
- [Flask-restful](https://flask-restful.readthedocs.io/en/latest/)
- [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)

## Improvement Opportunities
- Implement Docker orchestration and build a Postgres or MongoDB container. 
- AWS Infrastructure configs could be exported for IAC tools
- Automated Testing using Pytest in the CircleCI build/deploy pipeline
- General code cleanliness improvements

