prefix=/usr
bindir=$(prefix)/bin
hubplugindir=$(prefix)/lib/koji-hub-plugins
builderplugindir=$(prefix)/lib/koji-builder-plugins


install-cli:
	mkdir -p $(DESTDIR)$(bindir)
	install -p -m 0755 cli/koji-mash-tree $(DESTDIR)$(bindir)

install-hub-plugin:
	mkdir -p $(DESTDIR)$(hubplugindir)
	install -p -m 0644 hub/kojihub_mash_handler.py $(DESTDIR)$(hubplugindir)

install-builder-plugin:
	mkdir -p $(DESTDIR)$(builderplugindir)
	install -p -m 0644 builder/kojibuilder_mash_task.py $(DESTDIR)$(builderplugindir)

install: install-cli install-hub-plugin install-builder-plugin
