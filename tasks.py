from invoke import task, Collection, Context

@task
def commit(ctx, message="init"):
    ctx.run("git add .")
    ctx.run(f'git commit -m "{message}"')

@task
def quit(ctx):
    print("Copyright © 2024 Charudatta")

@task
def test(ctx):
    ctx.run("python -m unittest discover -s tests")

@task
def run_api(ctx):
    ctx.run("python src/app.py")

@task
def run_cli(ctx):
    ctx.run("python src/cli.py")

@task(default=True)
def default(ctx):
    tasks = sorted(ns.tasks.keys())
    for i, task_name in enumerate(tasks, 1):
        print(f"{i}: {task_name}")
    choice = int(input("Enter the number of your choice: "))
    ctx.run(f"invoke {tasks[choice - 1]}")

ns = Collection(
    commit,
    quit,
    test,
    run_api,
    run_cli,
    default,
)
