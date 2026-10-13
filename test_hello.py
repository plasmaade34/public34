import subprocess
import sys

def test_hello_output():
    result = subprocess.run([sys.executable, "hello.py"], capture_output=True, text=True, check=True)
    assert result.stdout == "Hello from Python!\n"
    assert result.stderr == ""
