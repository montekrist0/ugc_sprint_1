from fastapi import FastAPI
import uvicorn

from api.v1 import view_progress


app = FastAPI(
    title='API для взаимодействия с брокером сообщений',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    description='Сообщения о времени остановки просмотра фильма',
    version='1.0.0'
)


app.include_router(view_progress.router, prefix='/api/v1')


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8001,
        reload=True
    )
