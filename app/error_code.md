# 200

200 0 Success(APIException) - success
201 0 AddSuccess(Success) - add success
202 1 DeleteSuccess(Success) - delete success

# 500

500 999 APIException(HTTPException) - server internal error
500 999 ServerError(APIException) - server internal error

# 400

400 1000 ParemeterError(APIException) - parameter error
404 1001 NotFoundError(APIException) - notfound error
401 1002 AuthError(APIException) - auth error - bad token
401 1003 AuthError(APIException) - auth error - token expired
403 1004 Forbidden(APIException) - forbidden

400 1006 ClientTypeError(APIException) - client type error
400 1007 ClientScopeError(APIException) - client scope error

405 2000 HTTPException - bad request
