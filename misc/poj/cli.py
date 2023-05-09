import click
import os
import shutil
import subprocess
import sys

COMPILE_CMD = "/usr/local/bin/g++-13 -std=c++98 -Wall"
CPP_TEMPLATE_PATH = "templates/template.cpp"


@click.group()
def cli():
    pass


@click.command("create")
@click.argument("id-num")
@click.option("--tests", default=1, help="Number of empty test input files to create")
def create(id_num, tests):
    if not os.path.exists(f"./{id_num}"):
        os.mkdir(f"./{id_num}")
        click.echo(f"Created dir ./{id_num}")

    problem_path = f"./{id_num}/{id_num}.cc"
    if not os.path.exists(problem_path):
        shutil.copyfile(CPP_TEMPLATE_PATH, problem_path)
        click.echo(f"Created template {problem_path}")

    for i in range(tests):
        test_path = f"./{id_num}/{id_num}_input{i}.txt"
        if not os.path.exists(test_path):
            open(test_path, "a").close()
            click.echo(f"Created empty {test_path}")


@click.command("build")
@click.argument("id-num")
def build(id_num):
    command = f"{COMPILE_CMD} ./{id_num}/{id_num}.cc -o /tmp/{id_num}.out"
    click.echo(command)
    cp = subprocess.run(command, shell=True)
    if cp.returncode != 0:
        sys.exit(cp.stdout)
    click.echo(f"Compiled ./{id_num}/{id_num}.cc.")
    click.echo(f"Bin path: /tmp/{id_num}.out")


@click.command("test")
@click.argument("id-num")
def test(id_num):
    exec_cmd = f"/tmp/{id_num}.out"
    input_files = subprocess.run(f"ls ./{id_num} | grep '{id_num}_input'",
                                 shell=True, capture_output=True, text=True).stdout
    test_inputs = [filename for filename in input_files.split('\n') if filename]
    for input_file in test_inputs:
        cmd = f"cat ./{id_num}/{input_file} | {exec_cmd}"
        click.echo(f"{cmd}")
        subprocess.run(cmd, shell=True)
        print(" ")


if __name__ == '__main__':
    cli.add_command(create)
    cli.add_command(build)
    cli.add_command(test)
    cli()
