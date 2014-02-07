import re

FIRST_CAP_REGEX = re.compile('(.)([A-Z][a-z]+)')
ALL_CAP_REGEX = re.compile('([a-z0-9])([A-Z])')


def to_underscore_style(camel_case):
    sub1 = FIRST_CAP_REGEX.sub(r'\1_\2', camel_case)
    return ALL_CAP_REGEX.sub(r'\1_\2', sub1).lower()


class AttrDict(dict):
    """Dictionary that allows for referencing keys as attributes."""

    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
