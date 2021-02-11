from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):
    """
    La interfaz Builder especifica métodos para crear las diferentes partes de
    los objetos Producto.
    """

    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class AceroBuilder(Builder):
    """
    Las clases de constructores concretos siguen la interfaz del constructor y proporcionan
    implementaciones específicas de los pasos de construcción. Tu programa puede tener
    Varias variaciones de Builders, implementadas de manera diferente.
    """

    def __init__(self) -> None:
        """
        Una instancia de generador nueva debe contener un objeto de producto en blanco, que es
        utilizado en el montaje posterior.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
 
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("Carroceria")

    def produce_part_b(self) -> None:
        self._product.add("Pertas")

    def produce_part_c(self) -> None:
        self._product.add("Tapa frontal o Capó")


class Product1():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes creadas: {', '.join(self.parts)}", end="")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
    
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    director = Director()
    builder = AceroBuilder()
    director.builder = builder

    print("Produccion de carroseria: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Produccion  final ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Creacion de partes perzonalizada: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()