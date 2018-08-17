import subprocess


def _(cmd):
    print(cmd)
    subprocess.check_call(cmd, shell=True)


if "{{cookiecutter.git_init}}" == "yes":
    _("git init")
    _("git add --all")
    _("git commit -m 'cookiecutter init'")
    _("git remote add origin {{cookiecutter.origin_url}}")
