from invoke import task

# STARTING TASK
@task
def start(ctx):
    ctx.run("python src/index.py")

# TESTING TASK
@task
def test(ctx):
    ctx.run("pytest src")

# COVERAGE TASKS
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")