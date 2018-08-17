# Yet Another Opinionated Package Cookiecutter

Another python package [cookiecutter][cookiecutter], focused on python packages with conda dependencies.

Opinions are like kittens...

[cookiecutter]: https://github.com/audreyr/cookiecutter

## Project Layout

A `src`-based layout ([ionelmc][ionelmc-layout], [hynek][hynek-layout]), distributing tests [as application code][pytest-layout].

[ionelmc-layout]: https://blog.ionelmc.ro/2014/05/25/python-packaging/
[hynek-layout]: https://hynek.me/articles/testing-packaging/
[pytest-layout]: https://docs.pytest.org/en/latest/goodpractices.html#choosing-a-test-layout-import-rules

## `.gitignore`

Hit-up [gitignore.io](https://www.gitignore.io/api/python).

## `setup.py`

Partially skeleton-ed from [kenneithreitz][kenneithreitz-setup].
Uses [setuptools_scm][setuptools_scm] for version management.

[kenneithreitz-setup]: https://github.com/kennethreitz/setup.py
[setuptools_scm]: https://github.com/pypa/setuptools_scm
