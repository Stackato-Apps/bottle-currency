import re
import os
import json
import types

def cfget(pattern, default=None, services=[]):
    """
    Get Stackato configuration option.
    
    @param pattern: a regular expression matching an option path
    @param default: default value if pattern is not matched
    @param service: the flattened option map; just leave it alone.

    The option map is constructed from the VCAP_SERVICES environment
    variable. A typical option path might look like this:

        /redis-2.2/0/credentials/hostname

    So, a Redis host name, for example, could be obtained this way:

        hostname = cfget(r'/redis.*/hostname', 'localhost')

    If more than one path matches the pattern, the shorter path wins.
    """
    if not services:
        load_service_map(services)
    rx = re.compile(pattern, re.U)
    for k, v in services:
        if rx.match(k):
            return v
    return default

def load_service_map(services):
    services_json = os.getenv('VCAP_SERVICES', '{}')
    vcap_struct = json.loads(services_json)
    flatten(services, vcap_struct)

def flatten(data, struct, path=''):
    data.append((path, struct))
    if isinstance(struct, types.DictType):
        for k, v in struct.items():
            flatten(data, v, path + '/' + unicode(k))
    elif (isinstance(struct, types.TupleType) or
          isinstance(struct, types.ListType)):
        for i, v in enumerate(struct):
            flatten(data, v, path + '/' + unicode(i))

