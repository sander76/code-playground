from structlog.testing import capture_logs
import structlog

_logger = structlog.get_logger()


def test_output():
    with capture_logs() as cap_logs:

        def raiser():
            raise ValueError("some error")

        try:
            raiser()
        except ValueError:
            _logger.exception("some error")
    print(cap_logs)
