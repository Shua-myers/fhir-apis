# To run:
```shell
uvicorn main:app --reload
```

- uvicorn: ASGI server
- main: the .py file where uvicorn should look for our code
- app: object created inside main (`app = FastAPI`)
- --reload: reload on code changes, for development only

# Notes
- I'd consider using [fhirstarter](https://pypi.org/project/fhirstarter/) if I was building this professionally