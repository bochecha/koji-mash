import logging

import koji


log = logging.getLogger("koji.plugin.kojihub_mash_handler")


def mash_tree(mash_target, build_tag, mash_opts, priority=None):
    """Mash the repository tree"""
    log.debug("Mashing '%s'..." % mash_target)

    # TODO: How to get the `context`?
    context.session.assertPerm("admin")

    task_opts = {'channel': 'mash'}
    if priority is not None:
        task_opts["priority"] = koji.PRIO_DEFAULT + priority

    # TODO: How to make the task?
    return make_task('mashTree', [mash_target, build_tag, mash_opts],
                     **task_opts)


# Export the handler so it is accessible through the Hub's XMLRPC API
mash_tree.exported = True
