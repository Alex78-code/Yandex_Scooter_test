import sender_stend_request
# Монахов Александр, 8-ая когорта, финальный проект. Инженер по тестированию плюс

# Функция для позитивной проверки
def positive_assert(track_order):
    # В переменную order_respons сохраняется результат запроса на получение заказа по треку
    order_response = sender_stend_request.get_order_track(track_order)
    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200


# Тест 1.
def test_get_order_track_success_response():
    positive_assert(sender_stend_request.track_order)
