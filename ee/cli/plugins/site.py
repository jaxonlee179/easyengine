"""EasyEngine site controller."""
from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook


def ee_site_hook(app):
    # do something with the ``app`` object here.
    pass


class EESiteController(CementBaseController):
    class Meta:
        label = 'site'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = ('site command manages website configuration'
                       'with the help of the following subcommands')
        arguments = [
            (['site_name'],
                dict(help='website name')),
            ]

    @expose(hide=True)
    def default(self):
        # TODO Default action for ee site command
        print("Inside EESiteController.default().")

    @expose(help="delete site example.com")
    def delete(self):
        # TODO Write code for ee site delete command here
        print("Inside EESiteController.delete().")

    @expose(help="enable site example.com")
    def enable(self):
        # TODO Write code for ee site enable command here
        print("Inside EESiteController.enable().")

    @expose(help="disable site example.com")
    def disable(self):
        # TODO Write code for ee site disable command here
        print("Inside EESiteController.disable().")

    @expose(help="get example.com information")
    def info(self):
        # TODO Write code for ee site info command here
        print("Inside EESiteController.info().")

    @expose(help="Monitor example.com logs")
    def log(self):
        # TODO Write code for ee site log command here
        print("Inside EESiteController.log().")

    @expose(help="Edit example.com's nginx configuration")
    def edit(self):
        # TODO Write code for ee site edit command here
        print("Inside EESiteController.edit().")

    @expose(help="Display example.com's nginx configuration")
    def show(self):
        # TODO Write code for ee site edit command here
        print("Inside EESiteController.show().")

    @expose(help="list sites currently available")
    def list(self):
        # TODO Write code for ee site list command here
        print("Inside EESiteController.list().")

    @expose(help="change to example.com's webroot")
    def cd(self):
        # TODO Write code for ee site cd here
        print("Inside EESiteController.cd().")


class EESiteCreateController(CementBaseController):
    class Meta:
        label = 'create'
        stacked_on = 'site'
        stacked_type = 'nested'
        description = 'create command manages website configuration with the \
                        help of the following subcommands'
        arguments = [
            (['site_name'],
                dict(help='the notorious foo option')),
            (['--html'],
                dict(help="html site", action='store_true')),
            (['--php'],
                dict(help="php site", action='store_true')),
            (['--mysql'],
                dict(help="mysql site", action='store_true')),
            (['--wp'],
                dict(help="wordpress site", action='store_true')),
            (['--wpsubdir'],
                dict(help="wpsubdir site", action='store_true')),
            (['--wpsubdomain'],
                dict(help="wpsubdomain site", action='store_true')),
            ]

    @expose(hide=True)
    def default(self):
        # TODO Default action for ee site command
        data = dict(foo='EESiteCreateController.default().')
        self.app.render((data), 'default.mustache')

        # print("Inside EESiteCreateController.default().")


class EESiteUpdateController(CementBaseController):
    class Meta:
        label = 'update'
        stacked_on = 'site'
        stacked_type = 'nested'
        description = 'update command manages website configuration with the \
                        help of the following subcommands'
        arguments = [
            (['site_name'],
                dict(help='website name')),
            (['--html'],
                dict(help="html site", action='store_true')),
            (['--php'],
                dict(help="php site", action='store_true')),
            (['--mysql'],
                dict(help="mysql site", action='store_true')),
            (['--wp'],
                dict(help="wordpress site", action='store_true')),
            (['--wpsubdir'],
                dict(help="wpsubdir site", action='store_true')),
            (['--wpsubdomain'],
                dict(help="wpsubdomain site", action='store_true')),
            ]

    @expose(help="update example.com")
    def default(self):
        # TODO Write code for ee site update here
        print("Inside EESiteUpdateController.default().")

        # site command Options and subcommand calls and definations to
        # mention here

        # If using an output handler such as 'mustache', you could also
        # render a data dictionary using a template.  For example:
        #
        #   data = dict(foo='bar')
        #   self.app.render(data, 'default.mustache')
        #
        #
        # The 'default.mustache' file would be loaded from
        # ``ee.cli.templates``, or ``/var/lib/ee/templates/``.
        #


def load(app):
    # register the plugin class.. this only happens if the plugin is enabled
    handler.register(EESiteController)
    handler.register(EESiteCreateController)
    handler.register(EESiteUpdateController)

    # register a hook (function) to run after arguments are parsed.
    hook.register('post_argument_parsing', ee_site_hook)
