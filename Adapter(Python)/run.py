class Target:
    """
    Define la interfaz especifica del dominio utilizada por el cliente
    """

    def request(self) -> str:
        return "Objetivo: el comportamiento del objetivo predeterminado."


class Adaptee:
    """
    El adaptador contiene un comportamiento útil, pero su interfaz es 
    incompatible con el código de cliente existente. El Adaptador necesita 
    alguna adaptación antes de que el código del cliente pueda usarlo.
    """

    def specific_request(self) -> str:
        return ".eetpada esalc al ed laicepse otneimatropmoc"


class Adapter(Target, Adaptee):
    """
    El adaptador hace que la interfaz del Adaptee sea compatible con la 
    interfaz del objetivo mediante herencia múltiple.
    """

    def request(self) -> str:
        return f"Adapter: (Trduccion) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    El código de cliente admite todas las clases que siguen la interfaz de destino.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Cliente: puedo trabajar bien con los objetos de destino:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: la clase Adaptee tiene una interfaz extraña. "
          "No se entiende:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Cliente: Pero puedo trabajar con él a través del Adaptador:")
    adapter = Adapter()
    client_code(adapter)

