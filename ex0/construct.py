
import sys
import os
import site


def is_venv() -> None:
    if sys.prefix == sys.base_prefix:

        print("\nMATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}\n"
              f"Virtual Environment: None detected\n")

        print("WARNING: You're in the global enviroment!\n"
              "The machines can see everything you install.\n")

        print("To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate #On Unix\n"
              "matrix_env\\Scripts\\activate #On Windows\n")

        print("Then run this program again.")
    else:
        venv_name = os.path.basename(sys.prefix)
        package_path = site.getsitepackages()[0]

        print("\nMATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}\n"
              f"Virtual Environment: {venv_name}\n"
              f"Enviroment Path: {sys.prefix}\n")

        print("SUCCESS: You're in an isolated environment!"
              "Safe to install packages without affecting\n"
              "the global system.\n")

        print(f"Package installation path:\n"
              f"{package_path}")


if __name__ == "__main__":
    is_venv()
