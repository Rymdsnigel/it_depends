import comparator

def test_get_dependency_from_line():
    dependency = comparator.get_dependency_from_line("dependency==1.2.3")
    assert dependency.name == "dependency"
    assert dependency.version == "1.2.3"

def test_get_dependency_from_line_no_version():
    dependency = comparator.get_dependency_from_line("dependency")
    assert dependency.name == "dependency"
    assert dependency.version == ""

def test_line_is_requirement():
	line_is_requirement = comparator.line_is_requirement("dependency==1.2.3")
	assert line_is_requirement is True

def test_line_is_requirement_is_comment():
	line_is_requirement = comparator.line_is_requirement("# Another requirement")
	assert line_is_requirement is False

def test_line_is_requirement_is_blank_line():
	line_is_requirement = comparator.line_is_requirement("")
	assert line_is_requirement is False