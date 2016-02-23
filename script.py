import comparator

print("Comparing dependecies...")

dependencies = comparator.parse_requirements('requirements.txt')

for dependency in dependencies:
    comparator.compare_dependency_to_pypi(dependency)
