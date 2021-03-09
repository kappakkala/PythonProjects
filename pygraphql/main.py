import uvicorn

if __name__ == "__main__":

    uvicorn.run("fastapp:app", host="xxx.xxx.xxx.xxx", port=8081, reload=True)
