import click
import os
import shutil
import subprocess
import sys

COMPILE_CMD = "/usr/local/bin/g++-13 -g -std=c++20 -Wall -Werror -DLOCAL"
# COMPILE_CMD += "-L/usr/local/Cellar/gperftools/2.10/lib/ -lprofiler -ltcmalloc"
CPP_TEMPLATE_PATH = "templates/template.cpp"
PYTHON_TEMPLATE_PATH = "templates/template.py"
CPP_EXE_PATH = "../bin"


@click.group()
def cli():
    pass


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


@click.command("create")
@click.argument("problem-id")
@click.option("--tests", default=1, help="Number of empty test input files to create")
@click.option("--python", is_flag=True, default=False, help="Create a Python template instead of CPP")
def create_cmd(problem_id, tests, python):
    create(problem_id, tests, python)


def build(problem_id):
    command = f"{COMPILE_CMD} ./{problem_id}/{problem_id}.cpp -o  {CPP_EXE_PATH}/{problem_id}.out"
    click.echo(command)
    cp = subprocess.run(command, shell=True)
    if cp.returncode != 0:
        sys.exit(cp.stdout)
    click.echo(f"Compiled ./{problem_id}/{problem_id}.cpp.")
    click.echo(f"Bin path: {CPP_EXE_PATH}/{problem_id}.out")


@click.command("build")
@click.argument("problem-id")
def build_cmd(problem_id):
    build(problem_id)


def test(problem_id, python, show_output):
    python_exec = f"time python3 ./{problem_id}/{problem_id}.py"
    cpp_exec = f"{CPP_EXE_PATH}/{problem_id}.out"
    # cpp_exec = f"CPUPROFILE={CPP_EXE_PATH}/{problem_id}.prof time -h" + cpp_exec
    exec_cmd = python_exec if python else cpp_exec
    input_files = subprocess.run(f"ls ./{problem_id} | grep '{problem_id}_input'",
                                 shell=True, capture_output=True, text=True).stdout
    test_inputs = [filename for filename in input_files.split('\n') if filename]
    for input_file in test_inputs:
        cmd = f"cat ./{problem_id}/{input_file} | {exec_cmd}"
        click.echo(f"{cmd}")
        subprocess.run(cmd, shell=True)
        print(" ")


@click.command("test")
@click.argument("problem-id")
@click.option("--python", is_flag=True, default=False, help="Look for Python executable instead of CPP")
@click.option("--show-output", is_flag=True, default=False, help="If enabled, will show program output")
def test_cmd(problem_id, python, show_output):
    test(problem_id, python, show_output)


def retry(problem_id, python, show_output):
    python = False
    if not python:
        build(problem_id)
    test(problem_id, python, show_output)


@click.command("retry")
@click.argument("problem-id")
@click.option("--python", is_flag=True, default=False, help="Look for Python executable instead of CPP")
@click.option("--show-output", is_flag=True, default=False, help="If enabled, will show program output")
def retry_cmd(problem_id, python, show_output):
    retry(problem_id, python, show_output)


if __name__ == '__main__':
    cli.add_command(create_cmd)
    cli.add_command(build_cmd)
    cli.add_command(test_cmd)
    cli.add_command(retry_cmd)
    cli()
