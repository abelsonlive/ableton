"""
Given a URL of a corporate details page, extract it's associated 
XML file and return a dictionary with camelcased fieldnames.
"""
# -*- coding: utf-8 -*-

from xml.etree import ElementTree
from collections import defaultdict
import re

# regexes to parse xml fieldnames to underscore.
first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def camel_case_to_underscore(name):
    """
    Covert a camel case string to underscore.
    """
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def clean_key(k):
    """
    Clean a key of the schema name.
    """
    k = re.sub('{http://ch.powernet.ch/schema/}', '', k)
    return k


def etree_to_dict(t):
    """
    Turn an XML etree into a dictoary.
    """
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.iteritems():
                k = camel_case_to_underscore(clean_key(k))
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.iteritems()}}
    if t.attrib:
        d[t.tag].update((camel_case_to_underscore(k), v)
                        for k, v in t.attrib.iteritems())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['text'] = text
        else:
            d[t.tag] = text
    return d


def to_dict(content):
    """
    Parse an XML file.
    """
    t = ElementTree.fromstring(content)
    return etree_to_dict(t)
