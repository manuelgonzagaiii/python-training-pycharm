"""Logging Failures: exc_info, traceback & sys.exc_info

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import logging, traceback
from errors import ERPError

def report_failure(logger: logging.Logger, exc: BaseException) -> str:
    code = exc.code if isinstance(exc, ERPError) else "unhandled"
    logger.error("operation failed [%s]", code, exc_info=exc)
    # TODO: build a readable report from traceback.TracebackException.from_exception(exc)
    #       (chain=True so __cause__/__context__ frames are included) and return it
    raise NotImplementedError
"""

# Your code here.
