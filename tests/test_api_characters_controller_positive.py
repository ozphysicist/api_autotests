from characters_controller.characters import Characters

import asserts


def test_get_characters_response_status_is_ok(characters: Characters) -> None:
    response = characters.characters_get()
    asserts.assert_equal(
        200,
        response.status_code,
        f'Ожидаемый ответ от сервиса - 200, фактический - {response.status_code}',
    )
