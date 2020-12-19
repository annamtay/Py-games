from src.coin_flip import stripping_answer, verify_user_response, coin_flip_game


def test_stripping_answer():
    unrefined_answer = '    HellO  '
    stripped_answer = stripping_answer(unrefined_answer)
    assert stripped_answer == "hello"


def test_user_response_unknown():
    user_answer = "I'm not sure"
    unverified_response = verify_user_response(user_answer)
    assert unverified_response == "unknown"


