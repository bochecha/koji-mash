# Copyright (c) 2013 - Mathieu Bridon
#
# This plugin is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This plugin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this plugin.  If not, see <http://www.gnu.org/licenses/>.


import koji
from koji.tasks import BaseTaskHandler


# FIXME: This is pretty disgusting
kojid = {"__name__": "anything but __main__"}
execfile("/usr/sbin/kojid", kojid)
BuildRoot = kojid["BuildRoot"]


class MashTreeTask(BaseTaskHandler):
    Methods = ['mashTree']
    _taskWeight = 2.0

    def handler(self, mash_target, build_tag, mash_opts):
        self.logger.debug("Mashing '%s'..." % mash_target)

        build_tag = self.session.getTag(build_tag, strict=True)

        repo = self.session.getRepo(build_tag["name"])
        host = self.session.host.getHost()
        build_config = self.session.getBuildConfig(build_tag["id"],
                                                   event=repo["create_event"])
        arch = self.find_arch("noarch", host, build_config)

        root = BuildRoot(self.session, self.options, build_tag["name"], arch,
                          self.id, repo_id=repo["id"], install_group='mash')
        root.workdir = self.workdir
        self.logger.debug("Initializing buildroot")
        root.init()

        mash_cmd = ["mash"]

        if "mash_config" in mash_opts:
            mash_cmd.extend(["--config", mash_opts["mash_config"]])
        if "output_dir" in mash_opts:
            mash_cmd.extend(["--outputdir", mash_opts["output_dir"]])
        if "previous_dir" in mash_opts:
            mash_cmd.extend(["--previous", mash_opts["previous_dir"]])
        if "delta_dir" in mash_opts:
            mash_cmd.extend(["--delta", mash_opts["delta_dir"]])
        if "comps_file" in mash_opts:
            mash_cmd.extend(["--compsfile", mash_opts["comps_file"]])
        if not mash_opts["do_delta"]:
            mash_cmd.append("--no-delta")

        mash_cmd.append(mash_target)

        from datetime import datetime
        begin = datetime.now()
        rv = root.mock(["--chroot", " ".join(mash_cmd)])
        if rv:
            root.expire()
            raise koji.BuildrootError("error mashing the tree, %s"
                                      % root._mockResult(rv, logfile="mock_output.log"))
        end = datetime.now()
        self.logger.error("Mash finished in %s" % (end - begin))

        # TODO: What to do with the mashed tree?
        #
        # We could try to upload it back...
        #mashed_dir = os.path.join(root.rootdir(),
        # TODO: Find a way to get to the outputdir (either from mash_opts or
        #       from the conf files **inside** the chroot)
        #                          "store/koji/mash/mashed/%s" % mash_target)
        #
        #self.logger.error("Uploading the results")
        #begin = datetime.now()
        #root.uploadDir(mashed_dir, recursive=True)
        #end = datetime.now()
        #self.logger.error("Upload finished in %s" % (end - begin))
        #
        # Or we could not do anything, and assume that the outputdir is
        # mounted read-write inside the chroot.
        # But mikem doesn't like that :-/

        return {"brootid": root.id}
