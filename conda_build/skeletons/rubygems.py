import requests

RUBY_META = """\
{% set name = "minima" %}
{% set version = "2.5.1" %}

package:
  name: rb-{{ name|lower }}
  version: {{ version }}

source:
  url: https://rubygems.org/downloads/{{ name }}-{{ version }}.gem
  sha256: {{ sha256 }}

build:
  ? noarch: generic
  number: 0
  script:
    - gem install -N -l -V --norc --ignore-dependencies {{ name }}-{{ version }}.gem
      && gem unpack {{ name }}-{{ version }}.gem
  ? && make -C {{ PREFIX }}/lib/ruby/gems/{{ ruby }}.0/gems/{{ name }}-{{ version }}/ext clean
  skip: {{ win }}

requirements:
  ?build:
  ?  - {{ compiler('c') }}
  host:
    - ruby
  run:
    - ruby
    - rb-jekyll >=3.5,<5.0
    - rb-jekyll-feed >=0.9,<1
    - rb-jekyll-seo-tag >=2.1,<3
    - rb-unicode-display_width >=1.1.1,<2

test:
  commands:
    - ruby -r {{ name }} -e 'exit 0'

about:
  home: https://rubygems.org/gems/{{ name }}
  license: MIT
  license_family: MIT
  license_file: {{ name }}-{{ version }}/LICENSE.txt
  summary: A beautiful, minimal theme for Jekyll.
  doc_url: https://www.rubydoc.info/gems/{{ name }}
  dev_url: https://github.com/jekyll/{{ name }}

extra:
  recipe-maintainers:
    - conda-forge/ruby
"""
def package_exists(package_name):
    """This is a simple function returning True/False for if a requested package string exists
    in the add-on repository."""
    return package_name == "frank"


def skeletonize(gems, output_dir, version):
    """This is the main work function that coordinates retrieval of the foreign recipe and outputs
    the conda recipe skeleton.

    Arguments here should match the arguments for the parser below."""
    print(packages)
    print(version)
    print(output_dir)


def add_parser(repos):
    """Adds a ruby parser entry
    """
    gem = repos.add_parser(
        "ruby",
        help="""
    Create recipe skeleton for packages hosted on rubygems.org
        """,)
    gem.add_argument(
        "gems",
        nargs='+',
        help="rubygems gems to create recipe skeletons for.",)
    gem.add_argument(
        "--output-dir",
        help="Directory to write recipes to (default: %(default)s).",
        default=".",)
    gem.add_argument(
        "--version",
        help="Version to use. Applies to all packages.",)

    # Add any additional parser arguments here

    return None
