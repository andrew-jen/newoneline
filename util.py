from datetime import datetime


def success(data=None, status_code=200):
    if data is None:
        return {"message": "success"}, status_code

    return {
        "message": "success",
        "data": data,
        "datatime": datetime.utcnow().isoformat(),
    }, status_code


def failure(data=None, status_code=500):
    if data is None:
        return {"message": "failure"}, status_code

    return {
        "message": "failure",
        "data": data,
        "datatime": datetime.utcnow().isoformat(),
    }, status_code