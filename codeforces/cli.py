import click
import os
import shutil
import subprocess
import sys

COMPILE_CMD = "/usr/local/bin/g++-13 -x c++ -O2 -std=c++17 -D__USE_MINGW_ANSI_STDIO=0 -Wall"  # -DLOCAL"
CPP_TEMPLATE_PATH = "templates/template.cpp"
PYTHON_TEMPLATE_PATH = "templates/template.py"


@click.group()
def cli():
    pass


def create(problemset, letter, tests, python):
    if not os.path.exists(f"./{problemset}"):
        os.mkdir(f"./{problemset}")
        click.echo(f"Created dir ./{problemset}")

    template_path = PYTHON_TEMPLATE_PATH if python else CPP_TEMPLATE_PATH
    problem_path = f"./{problemset}/{letter}.{'py' if python else 'cpp'}"
    if not os.path.exists(problem_path):
        shutil.copyfile(template_path, problem_path)
        click.echo(f"Created template {problem_path}")

    for i in range(tests):
        test_path = f"./{problemset}/{letter}_input{i}.txt"
        if not os.path.exists(test_path):
            open(test_path, "a").close()
            click.echo(f"Created empty {test_path}")


@click.command("create")
@click.argument("problemset")
@click.argument("letter")
@click.option("--tests", default=1, help="Number of empty test input files to create")
@click.option("--python", is_flag=True, default=False, help="Create a Python template instead of CPP")
def create_cmd(problemset, letter, tests, python):
    create(problemset, letter, tests, python)


def build(problemset, letter):
    command = f"{COMPILE_CMD} ./{problemset}/{letter}.cpp -o /tmp/{problemset}-{letter}.out"
    click.echo(command)
    cp = subprocess.run(command, shell=True)
    if cp.returncode != 0:
        sys.exit(cp.stdout)
    click.echo(f"Compiled ./{problemset}/{letter}.cpp.")
    click.echo(f"Bin path: /tmp/{problemset}-{letter}.out")


@click.command("build")
@click.argument("problemset")
@click.argument("letter")
def build_cmd(problemset, letter):
    build(problemset, letter)


def test(problemset, letter, python):
    exec_cmd = f"python3 ./{problemset}/{letter}.py" if python else f"/tmp/{problemset}-{letter}.out"
    input_files = subprocess.run(f"ls ./{problemset} | grep '{letter}_input'",
                                 shell=True, capture_output=True, text=True).stdout
    test_inputs = [filename for filename in input_files.split('\n') if filename]
    for input_file in test_inputs:
        cmd = f"cat ./{problemset}/{input_file} | {exec_cmd}"
        click.echo(f"{cmd}")
        subprocess.run(cmd, shell=True)
        print(" ")


@click.command("test")
@click.argument("problemset")
@click.argument("letter")
@click.option("--python", is_flag=True, default=False, help="Look for Python executable instead of CPP")
def test_cmd(problemset, letter, python):
    test(problemset, letter, python)


@click.command("retry")
@click.argument("problemset")
@click.argument("letter")
@click.option("--python", is_flag=True, default=False, help="Look for Python executable instead of CPP")
def retry_cmd(problemset, letter, python):
    build(problemset, letter)
    test(problemset, letter, python)


if __name__ == '__main__':
    cli.add_command(build_cmd)
    cli.add_command(create_cmd)
    cli.add_command(retry_cmd)
    cli.add_command(test_cmd)
    cli()
