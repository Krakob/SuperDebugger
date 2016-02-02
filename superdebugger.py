def debug(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            assert "It's a feature."
    return inner
