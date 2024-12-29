import yaml

from jinja2 import Environment, FileSystemLoader
from pathlib import Path


template_name = "template_tmpl.jinja2"
definition_name = "definition.yaml"
generated_name = "generated.cpp"


def get_definition(template_dir_path: Path):
    with open(template_dir_path / definition_name, "r") as f:
        data = yaml.safe_load(f)
    return data


def generate(template_dir_path: Path):
    definition = get_definition(template_dir_path)

    environment = Environment(
        loader=FileSystemLoader(template_dir_path),
        trim_blocks=True,
        lstrip_blocks=True
    )

    content = environment.get_template(template_name).render(message=definition["class"])
    with open(template_dir_path / generated_name, mode="w") as f:
        f.write(content)
