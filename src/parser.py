import argparse

from . import templates_dir_path


class TemplateAction(argparse.Action):
    def __call__(self, parser, namespace, value, *args, **kwargs):
        template_path = templates_dir_path / value

        if not template_path.is_dir():
            parser.error(f"Template dir {value} not found")
        setattr(namespace, self.dest, template_path)


def parse():
    parser = argparse.ArgumentParser(
        prog="c++ codegen",
        description="console client is used to generate c++ boilerplate code from a template."
    )
    parser.add_argument(
        "--template",
        help="template dir for %(prog)s", action=TemplateAction,
        required=True
    )
    args = parser.parse_args()
    return args
