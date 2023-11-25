from invoke import task


@task
def format(ctx):
    ctx.run("isort .")
    ctx.run("black .")


@task
def coverage(ctx):
    ctx.run("pytest --cov=src --cov-report html")


@task
def mypy(ctx):
    ctx.run("mypy src")
