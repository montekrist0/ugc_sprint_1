from fastapi import APIRouter, Depends, HTTPException, Response
from http import HTTPStatus

from api.v1.models import ViewProgress
from core.configs import ProducerError
from services.view import ViewService, get_view_service


router = APIRouter()


@router.post(
    "/{film_id}/view_progress",
    summary="Сообщение о просмотре фильма",
    description="Сообщение о просмотре фильма",
    tags=["view"],
)
async def view_progress(view_progress_params: ViewProgress, view_service: ViewService = Depends(get_view_service)):
    """
    Метод (ручка) для отправки сообщений о процессе просмотре фильма

    :param view_progress_params: id фильма, id пользователя, value: данные для отправки
    :param view_service: класс движка для отправки сообщений в топик view
    :return: список документов в виде Pydantic класса
    """
    try:
        await view_service.send(*view_progress_params.dict().values())
        return Response(content="Message successfully delivered")

    except ProducerError:
        raise HTTPException(
            status_code=HTTPStatus.SERVICE_UNAVAILABLE, detail="service error. message was not delivered"
        )
