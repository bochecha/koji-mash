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

install: install-cli install-hub-plugin
