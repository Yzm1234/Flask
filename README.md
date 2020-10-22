# FlaskDemo
This an API practice project using Flask in Python. This demo is using Python3 (Python 3.7.1).

## Installation

`$ pip install -r requirements.txt`

## Usage
### 1. start the API server
Run `$ ./api.py` or `$ Python3 api.py` to start the server.
If it is successfully started, you will get the url: http://127.0.0.1:5000/.
The server has two directories, "/" and "/pokemon". <br/> "/" only allows GET method while "/pokemon" allows GET, PUT and POST methods.

### 2. Test the API server
There are two ways to test the api.py file
- 1. Run `$ ./api_test.py` or `$ Python3 api_test.py` in command line. 
- 2. Use Curl.
For example:
to test the POST method for http://127.0.0.1:5000/pokemon.
Run  
`$ curl -d "key=key1&value=5" -X POST http://127.0.0.1:5000/pokemon`
You will get an echo like:
```
{
  "echo": {
    "key": "key1", 
    "value": "5"
  }
}
```


