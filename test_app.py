import os
import tempfile

import pytest

import app

@pytest.fixture
def client():
    db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    
   
    yield client
    os.close(db_fd)
    os.unlink(app.app.config['DATABASE'])



def test_home(client):
    response=client.get("/")
    with open("see.txt","wb+") as f:
        f.write(response.data)
    assert b"Feature Request" in response.data


def test_add(client):
    response=client.get("/add/features/", follow_redirects=True)
    assert b"Feature Request" in response.data

    response=client.post("/add/features/",data=dict(
        title="title",
        description="description",
        client_priority="1",
        client="Client A",
        date="2020-10-10"
    ),follow_redirects=True)
    assert b"1" in response.data

    response=client.post("/add/features/",data=dict(
        title="title",
        description="description",
        client_priority="1",
        client="Client A",
        date="2020-10-10"
    ),follow_redirects=True)

    assert b"2" in response.data

