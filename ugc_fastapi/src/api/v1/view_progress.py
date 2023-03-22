from api.v1.models import ViewProgress
from services.view import ViewService, get_view_service

from fastapi import APIRouter, Depends

router = APIRouter()


@router.post('/{film_id}/view_progress',
             summary='Сообщение о просмотре фильма',
             description='Сообщение о просмотре фильма',
             tags=['view'])
async def view_progress(view_progress_params: ViewProgress,
                        view_service: ViewService = Depends(get_view_service)):
    """
    Метод (ручка) для отправки сообщений о процессе просмотре фильма

    :param view_progress_params: id фильма, id пользователя, value: данные для отправки
    :param view_service: класс движка для отправки сообщений в топик view
    :return: список документов в виде Pydantic класса
    """
    await view_service.send(*view_progress_params.dict().values())
