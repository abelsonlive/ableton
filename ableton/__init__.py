import gzip
import json

from ableton import xml_util


class Ableton:

    def __init__(self, fp, **kw):
        with gzip.open(fp, 'r') as fh:
            contents = fh.read()
        print json.dumps(xml_util.to_dict(contents))
