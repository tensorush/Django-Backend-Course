def application(environment, start_response):
    data = b"All your codebase are belong to us.\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
