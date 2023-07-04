from werkzeug.exceptions import HTTPException


class QuantityExceptionItems(HTTPException):
    code = 400
