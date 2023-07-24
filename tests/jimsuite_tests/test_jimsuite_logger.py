from src.libs.jimsuite import jimsuite_logger as logger

import pytest

@pytest.mark.parametrize("new_level, raise_error", [
    ("EXIT", False),
    ("CRITICAL", False),
    ("ERROR", False),
    ("WARNING", False),
    ("MAIN", False),
    ("CHECK", False),
    ("BOOT", False),
    ("PROGRAM", False),
    ("INFO", False),
    ("DEBUG", False),
    ("NOTSET", False),
    (4324, False),
    (0.0, True),
    (-10, True),
])
def test_change_threshold_level(new_level, raise_error):
    if not raise_error:
        logger.change_threshold_level(new_level)
    else:
        with pytest.raises(SystemExit):
            logger.change_threshold_level(new_level)

@pytest.mark.parametrize("text", [
    "Test",
    3,
    3.1,
    True,
    False,
    -1
])
def test_prints(capsys, text):
    # Setup
    logger.change_threshold_level(new_level="NOTSET")
    capsys.readouterr()
    
    logger.none(f"{text}")
    captured = capsys.readouterr()
    assert captured.out == f"{text}\n"

    logger.program(f"{text}")
    captured = capsys.readouterr()
    assert captured.out == f"PROG: {text}\n"

    logger.boot(f"{text}")
    captured = capsys.readouterr()
    assert captured.out == f"BOOT: {text}\n"

    logger.main(f"{text}")
    captured = capsys.readouterr()
    assert captured.out == f"MAIN: {text}\n"

    logger.check(f"{text}")
    captured = capsys.readouterr()
    assert captured.out == f"CHCK: {text}\n"

    logger.debug(f"{text}")
    captured = capsys.readouterr()
    assert captured.out == f"DBUG: {text}\n"

    logger.warning(f"{text}")
    captured = capsys.readouterr()
    assert captured.out == f"WARN: {text}\n"

    logger.info(f"{text}")
    captured = capsys.readouterr()
    assert captured.out == f"INFO: {text}\n"

    with pytest.raises(SystemExit) as error:
        logger.error(f"{text}")
    assert error.value.code == f"ERRO: {text}"

    logger.critical(f"{text}")
    captured = capsys.readouterr()
    assert captured.out == f"CRIT: {text}\n"

    with pytest.raises(SystemExit) as error:
        raise logger.exit(f"{text}")
    assert error.value.code == f"EXIT: {text}"

