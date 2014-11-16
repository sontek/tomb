from pyramid.scaffolds import PyramidTemplate


class BaseTombTemplate(PyramidTemplate):
    _template_dir = 'template/'
    summary = 'The base tomb template'

    def post(self, command, output_dir, vars):
        self.out('Created new tomb project here: %s' % output_dir)
