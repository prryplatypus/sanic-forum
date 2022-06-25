class BaseModel(object):
    def to_dict(self) -> dict:
        raise NotImplementedError()
