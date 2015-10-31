from collections import namedtuple
import json

import requests

Dependency = namedtuple('Dependency', ['name', 'version'])


def get_dependency_from_line(line):
    dep = line.strip().split('==')
    name = dep[0]
    try:
        version = dep[1]
    except IndexError:
        version = ''
    return Dependency(name=name, version=version)


def parse_requirements(path):
    dependencies = set([])
    try:
        with open(path) as requirements:
            for line in requirements:
                if len(line) > 1:
                    if line.find('#'):
                        dependencies.add(get_dependency_from_line(line))
    except IOError as e:
        print 'Error reading file: %s' % e.strerror
    return dependencies


def get_dependency_from_pypi(dependency):
    pypi_url = 'http://pypi.python.org/pypi/{0}/json'.format(dependency)
    response = requests.get(pypi_url)
    return response.json()


def get_latest_version(dependency_json):
    return dependency_json[u'info'][u'version']


def compare_dependency_to_pypi(dependency):
    project_dep_version = dependency.version
    latest_version = get_latest_version(get_dependency_from_pypi(dependency.name))
    print "{0} is at {1} in project, current stable is {2}".format(
        dependency.name,
        project_dep_version,
        latest_version)

print("Comparing dependecies...")

dependencies = parse_requirements('requirements.txt')

for dependency in dependencies:
    compare_dependency_to_pypi(dependency)
