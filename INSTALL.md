Deployment is a three-part process, as their are three components to install.

One thing to note are the requirements:

* Koji >= 1.8.0 (things might work with older versions, but this is the
                 earliest one we've ever tested)
* mash >= 0.6.02 (for the `--no-delta` option)

## Deploying the Hub plugin

First, install the plugin:

```
$ sudo make install-hub-plugin
```

Next, tell the Koji Hub to use it, by adding `kojihub_mash_handler` to the
`Plugins =` line in `/etc/koji-hub/hub.conf`.

Now restart the Hub.

Finally, you must create a `mash` channel and add your builders to it:

```
$ koji -c /etc/koji.networkbox.conf add-host-to-channel --new <builder> mash
```

## Deploying the Builder plugin

First, install the plugin:

```
$ sudo make install-builder-plugin
```

Next, tell the Koji Builder to use it, by adding `kojibuilder_mash_task` to
the `plugins =` line in `/etc/kojid/kojid.conf`.

Finally, restart the Builder.

## Deploying the command-line tool

This is the simplest part:

```
$ sudo make install-cli
```

And that's it.
