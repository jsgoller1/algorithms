import click
import os
import shutil
import subprocess
import sys

COMPILE_CMD = "/usr/local/bin/g++-13 -std=c++20 -O2 -Wall"
CPP_TEMPLATE_PATH = "templates/template.cpp"
PYTHON_TEMPLATE_PATH = "templates/template.py"


@click.group()
def cli():
    pass


@click.command("create")
@click.argument("problem-id")
@click.option("--tests", default=1, help="Number of empty test input files to create")
@click.option("--python", is_flag=True, default=False, help="Create a Python template instead of CPP")
def create(problem_id, tests, python):
    if not os.path.exists(f"./{problem_id}"):
        os.mkdir(f"./{problem_id}")
        click.echo(f"Created dir ./{problem_id}")

    template_path = PYTHON_TEMPLATE_PATH if python else CPP_TEMPLATE_PATH
    problem_path = f"./{problem_id}/{problem_id}.{'py' if python else 'cpp'}"
    if not os.path.exists(problem_path):
        shutil.copyfile(template_path, problem_path)
        click.echo(f"Created template {problem_path}")

    for i in range(tests):
        test_path = f"./{problem_id}/{problem_id}_input{i}.txt"
        if not os.path.exists(test_path):
            open(test_path, "a").close()
            click.echo(f"Created empty test {test_path}")
        solution_path = f"./{problem_id}/{problem_id}_expected{i}.txt"
        if not os.path.exists(solution_path):
            open(solution_path, "a").close()
            click.echo(f"Created empty solution {solution_path}")


@click.command("build")
@click.argument("problem-id")
def build(problem_id):
    command = f"{COMPILE_CMD} ./{problem_id}/{problem_id}.cpp -o /tmp/{problem_id}-{problem_id}.out"
    click.echo(command)
    cp = subprocess.run(command, shell=True)
    if cp.returncode != 0:
        sys.exit(cp.stdout)
    click.echo(f"Compiled ./{problem_id}/{problem_id}.cpp.")
    click.echo(f"Bin path: /tmp/{problem_id}-{problem_id}.out")


@click.command("test")
@click.argument("problem-id")
@click.option("--python", is_flag=True, default=False, help="Look for Python executable instead of CPP")
@click.option("--show-output", is_flag=True, default=False, help="If enabled, will show program output")
def test(problem_id, python, show_output):
    exec_cmd = f"python3 ./{problem_id}/{problem_id}.py" if python else f"/tmp/{problem_id}-{problem_id}.out"
    input_files = subprocess.run(f"ls ./{problem_id} | grep '{problem_id}_input'",
                                 shell=True, capture_output=True, text=True).stdout
    test_inputs = [filename for filename in input_files.split('\n') if filename]
    for input_file in test_inputs:
        cmd = f"cat ./{problem_id}/{input_file} | {exec_cmd}"
        click.echo(f"{cmd}")
        subprocess.run(cmd, shell=True)
        print(" ")


if __name__ == '__main__':
    cli.add_command(create)
    cli.add_command(build)
    cli.add_command(test)
    cli()
