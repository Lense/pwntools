"""Describes a way to submit a key to a key server.
"""
from __future__ import absolute_import

from pwnlib.args import args
from pwnlib.log import getLogger
from pwnlib.util.misc import write

log = getLogger(__name__)


def submit_flag(flag):
    env_file = args['FLAG_FILE'].strip()
    exploit = args['EXPLOIT_NAME'].strip()
    target = args['TARGET_HOST'].strip()
    team = args['TEAM_NAME'].strip()

    flag = flag.strip()

    log.success("Flag: %r" % flag)

    data = "\n".join([flag,
                      exploit,
                      target,
                      team,
                      ''])

    write(env_file, data)
