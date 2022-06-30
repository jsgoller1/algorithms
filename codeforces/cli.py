import click
import os
import shutil
import subprocess
import sys

COMPILE_CMD = "g++ -static -DLOCAL -lm -s -x c++ -O2 -std=c++17 -D__USE_MINGW_ANSI_STDIO=0 -Wall"
TEMPLATE_PATH = "tools/template.cpp"

@click.group()
def cli():
    pass

@click.command("create")
@click.option("--tests", default=1, help="Number of empty test input files to create")
@click.argument("problemset")
@click.argument("letter")
def create(problemset, letter, tests):
    if not os.path.exists(f"./{problemset}"):
        os.mkdir(f"./{problemset}")
        click.echo(f"Created dir ./{problemset}")
    if not os.path.exists(f"./{problemset}/{letter}.cpp"):
        shutil.copyfile(TEMPLATE_PATH, f"./{problemset}/{letter}.cpp")
        click.echo(f"Created template ./{problemset}/{letter}.cpp")
    for i in range(tests):
        test_path = f"./{problemset}/{letter}_input{i}.txt"
        if not os.path.exists(test_path):
            open(test_path, "a").close()
            click.echo(f"Created empty {test_path}")

@click.command("build")
@click.argument("problemset")
@click.argument("letter")
def build(problemset, letter):
    cp = subprocess.run(f"{COMPILE_CMD} ./{problemset}/{letter}.cpp -o /tmp/{problemset}-{letter}.out", shell=True)
    if cp.returncode != 0:
        sys.exit(cp.stdout)
    click.echo(f"Compiled ./{problemset}/{letter}.cpp.")
    click.echo(f"Bin path: /tmp/{problemset}-{letter}.out")


@click.command("test")
@click.argument("problemset")
@click.argument("letter")
def test(problemset, letter):
    cp = subprocess.run(f"ls ./{problemset} | grep '{letter}_input'", shell=True, capture_output=True, text=True)
    test_inputs = [filename for filename in cp.stdout.split('\n') if filename]
    for input_file in test_inputs:
            cmd = f"cat ./{problemset}/{input_file} | /tmp/{problemset}-{letter}.out"
            click.echo(f"{cmd}")
            subprocess.run(cmd, shell=True)
            print(" ")


if __name__ == '__main__':
    cli.add_command(create)
    cli.add_command(build)
    cli.add_command(test)
    cli()
