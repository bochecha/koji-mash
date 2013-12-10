## Mashing the Fedora repositories in Koji

The Fedora repositories are mashed with a set of ad-hoc scripts.

This project aims at replacing those scripts.

We provide 3 things:

* A Koji Builder plugin, which adds the new mash task.
* A Koji Hub plugin, which exposes the new mash task through the Hub's
  XMLRPC API.
* A command-line tool, which calls the Hub through XMLRPC, requesting that
  repositories be mashed.

The latter is optional, feel free to directly query the Koji Hub in your own
scripts via XMLRPC. ;-)

## Legalities

The 2 plugins and the command line tool are offered under the terms of the
[GNU Lesser General Public License, version 2.1 or any later version](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).

We won't ask you to sign a copyright assignment or any other kind of silly and
tedious legal document, so just send us patches and/or pull requests!
