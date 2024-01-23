# To run:
```shell
uvicorn main:app --reload
```

- uvicorn: ASGI server
- main: the .py file where uvicorn should look for our code
- app: object created inside main (`app = FastAPI`)
- --reload: reload on code changes, for development only
