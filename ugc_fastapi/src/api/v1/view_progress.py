
from services.view import ViewService, get_view_service

from fastapi import APIRouter, Depends

router = APIRouter()


@router.get('/{film_id}/view_progress',
            summary='Сообщение о просмотре фильма',
            description='Сообщение о просмотре фильма',
            tags=['view']
            )
async def view_progress(film_id: str, user_id: str, value: str,
                        view_service: ViewService = Depends(get_view_service)):
    """
    Метод (ручка) для отправки сообщений о процессе просмотре фильма

    :param film_id: id фильма
    :param user_id: id пользователя
    :param value: данные для отправки
    :param view_service: класс движка для отправки сообщений в топик view
    :return: список документов в виде Pydantic класса
    """
    await view_service.send(film_id, user_id, value)
