%w(
	.ruby_version
	.rbenv_vars
	tmp/restart.txt
	tmp/caching-dev.txt
).each { |path| Spring.watch(path) }
