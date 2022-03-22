from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to PyBites' FastAPI Learning Path 🐍 🎉"}


def main():
    print('please look after Mama and Naia')


if __name__ == '__main__':
    main()
