from pathlib import Path

from chainlit.cli import run_chainlit


def run():
    """Python entrypoint to run chainlit server.

    Used to provide a script via poetry.

    """
    run_chainlit(Path(Path(__file__).parent, "server.py").as_posix())
