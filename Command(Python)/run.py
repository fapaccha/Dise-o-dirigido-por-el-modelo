from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    La interfaz command declara un método para ejecutar un comando.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
   Algunos comandos pueden implementar operaciones simples por sí mismos.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: Con este metodo probamos que  command se puede utilizar con algo tan simple como imprimir un mensaje"
              f"({self._payload})")


class ComplexCommand(Command):
    """
    Sin embargo, algunos comandos pueden delegar operaciones más complejas a otros
    objetos, llamados "receptores".
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Los comandos complejos pueden aceptar uno o varios objetos receptores junto con
        cualquier dato de contexto a través del constructor.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Los comandos pueden delegar a cualquier método de un receptor.        """

        print("ComplexCommand: las cosas complejas deben ser realizadas por un objeto receptor", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """
    Las clases Receiver contienen una lógica empresarial importante. Ellos saben como
    realizar todo tipo de operaciones, asociadas a la realización de una solicitud. En
    De hecho, cualquier clase puede servir como Receptor.
    """

    def do_something(self, a: str) -> None:
        print(f"\nSe estan realizando trabajos en : ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\ntambien en:({b}.)", end="")


class Invoker:
    """
    El invocador está asociado con uno o varios comandos. Envía una solicitud
    al comando.
    """

    _on_start = None
    _on_finish = None

    """
    Inicializar comandos.

    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        El Invoker no depende de clases concretas de comandos o receptores. el 
        invocador pasa una solicitud a un receptor de forma indirecta, ejecutando un
        comando.
        """

        print("Se requiere realizar alguna operacion antes que se inicie?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()


        print("Se requiera hacer algo al terminar?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    El código del cliente puede parametrizar un invocador con cualquier comando.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Hola!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Enviando trabajo", "descarga de archivos"))

    invoker.do_something_important()