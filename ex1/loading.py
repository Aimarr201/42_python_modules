
import importlib
from typing import Any


def package_version(name: str) -> str:
    try:
        metadata = importlib.import_module("importlib.metadata")
        return str(metadata.version(name))
    except Exception:
        return "unknown"


def print_dependency_status(name: str, module: Any, description: str) -> None:
    if module is None:
        print(f"  [MISSING] {name} - install with: "
              "pip install -r requirements.txt\n"
              "                                   or: poetry install")
    else:
        print(f"  [OK] {name} ({package_version(name)}) - {description}")


def check_dependencies(packages: dict[str, str]) -> dict[str, Any | None]:
    print("Checking dependencies:")

    modules: dict[str, Any | None] = {}

    for package_name in packages:
        try:
            module = importlib.import_module(package_name)
        except Exception:
            module = None

        modules[package_name] = module
        print_dependency_status(package_name, module, packages[package_name])

    return modules


def import_package(name: str) -> Any | None:
    try:
        return importlib.import_module(name)
    except Exception:
        return None


def analyze_matrix_data(pandas: Any, numpy: Any, pyplot: Any) -> None:
    print("Analyzing Matrix data...\n"
          "Processing 1000 data points...\n")

    ciclos = numpy.arange(1000)
    ruido = numpy.sin(ciclos / 50.0) * 10 + numpy.random.normal(0, 3, 1000)

    print("Generating visualization...\n")

    df = pandas.DataFrame({"Anomalías (Crudo)": ruido}, index=ciclos)
    df["Patrón/Tendencia"] = df["Anomalías (Crudo)"].rolling(40).mean()

    pyplot.style.use('dark_background')
    pyplot.figure(figsize=(10, 5))

    pyplot.plot(df["Anomalías (Crudo)"], color='#004400',
                alpha=0.6, label="Ruido del Código")
    pyplot.plot(df["Patrón/Tendencia"], color='#00ff00',
                linewidth=2, label="Patrón de Anomalías")

    pyplot.title("Análisis del Código de Matrix - Detección de Anomalías",
                 color='#00ff00')
    pyplot.xlabel("Ciclos de Simulación", color='#00ff00')
    pyplot.ylabel("Intensidad de la Anomalía", color='#00ff00')
    pyplot.legend(loc="upper right")
    pyplot.grid(color='#003300', linestyle=':', alpha=0.5)

    pyplot.savefig("matrix_analysis.png", bbox_inches='tight')
    pyplot.close()

    print("Analysis complete!\n"
          "Results saved to: matrix_analysis.png")


def main() -> int:
    print("LOADING STATUS: Loading programs...\n")

    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }

    modules = check_dependencies(packages)

    print()

    if any(modules[package_name] is None for package_name in packages):
        return 0

    pandas = modules["pandas"]
    numpy = modules["numpy"]
    pyplot = import_package("matplotlib.pyplot")

    analyze_matrix_data(pandas, numpy, pyplot)
    return 0


if __name__ == "__main__":
    main()
