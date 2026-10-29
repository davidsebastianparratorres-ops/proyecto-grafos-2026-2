"""
Pruebas para Vertex.lower_cost_link()

Ubicación sugerida:  <raiz_del_proyecto>/tests/test_vertex_lower_cost_link.py
Ejecución (desde la raíz del proyecto):  python tests/test_vertex_lower_cost_link.py

Contrato que se asume (deducido de tu código actual):
  - links es un dict {destino: [costo1, costo2, ...]}  (add_link acumula en lista)
  - lower_cost_link() devuelve una tupla (destino, costo) con la arista más barata
"""
import os
import sys
import traceback
import unittest

# Permite ejecutar el archivo directamente: agrega la raíz del proyecto al path
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if RAIZ not in sys.path:
    sys.path.insert(0, RAIZ)

from src.models.Vertex import Vertex  # noqa: E402


def crear_vertice(tag="A", enlaces=()):
    """Crea un Vertex y le agrega enlaces [(destino, peso), ...] usando add_link."""
    v = Vertex(tag)
    for destino, peso in enlaces:
        v.add_link(destino, peso)
    return v


class TestLowerCostLink(unittest.TestCase):

    # ---------- casos básicos ----------
    def test_01_un_solo_enlace(self):
        v = crear_vertice("A", [("B", 5)])
        self.assertEqual(v.lower_cost_link(), ("B", 5))

    def test_02_menor_en_el_medio(self):
        v = crear_vertice("A", [("B", 7), ("C", 2), ("D", 9)])
        self.assertEqual(v.lower_cost_link(), ("C", 2))

    def test_03_menor_en_el_primer_destino(self):
        v = crear_vertice("A", [("B", 1), ("C", 4), ("D", 9)])
        self.assertEqual(v.lower_cost_link(), ("B", 1))

    def test_04_menor_en_el_ultimo_destino(self):
        v = crear_vertice("A", [("B", 8), ("C", 4), ("D", 1)])
        self.assertEqual(v.lower_cost_link(), ("D", 1))

    # ---------- varios costos hacia un mismo destino ----------
    def test_05_destino_con_varios_costos_gana_el_menor_de_ese_destino(self):
        v = crear_vertice("A", [("B", 10), ("B", 3), ("B", 6), ("C", 5)])
        self.assertEqual(v.lower_cost_link(), ("B", 3))

    def test_06_destino_con_varios_costos_pero_gana_otro_destino(self):
        v = crear_vertice("A", [("B", 10), ("B", 8), ("C", 2)])
        self.assertEqual(v.lower_cost_link(), ("C", 2))

    # ---------- valores especiales ----------
    def test_07_costo_cero(self):
        v = crear_vertice("A", [("B", 3), ("C", 0), ("D", 5)])
        self.assertEqual(v.lower_cost_link(), ("C", 0))

    def test_08_costos_negativos(self):
        v = crear_vertice("A", [("B", -1), ("C", -7), ("D", 2)])
        self.assertEqual(v.lower_cost_link(), ("C", -7))

    def test_09_costos_decimales(self):
        v = crear_vertice("A", [("B", 2.5), ("C", 2.49), ("D", 3.1)])
        self.assertEqual(v.lower_cost_link(), ("C", 2.49))

    def test_10_empate_el_costo_devuelto_es_el_minimo(self):
        # Con empate, qué destino se devuelve es decisión tuya; solo se valida el costo.
        v = crear_vertice("A", [("B", 4), ("C", 4), ("D", 9)])
        destino, costo = v.lower_cost_link()
        self.assertEqual(costo, 4)
        self.assertIn(destino, ("B", "C"))

    # ---------- forma del retorno y efectos secundarios ----------
    def test_11_retorna_tupla_de_dos_elementos(self):
        v = crear_vertice("A", [("B", 5), ("C", 2)])
        resultado = v.lower_cost_link()
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(len(resultado), 2)

    def test_12_el_costo_retornado_no_es_none(self):
        v = crear_vertice("A", [("B", 5)])
        _, costo = v.lower_cost_link()
        self.assertIsNotNone(costo)

    def test_13_no_modifica_los_enlaces(self):
        v = crear_vertice("A", [("B", 5), ("B", 2), ("C", 9)])
        antes = {k: list(c) for k, c in v.links.items()}
        v.lower_cost_link()
        despues = {k: list(c) for k, c in v.links.items()}
        self.assertEqual(antes, despues)

    def test_14_llamarla_dos_veces_da_el_mismo_resultado(self):
        v = crear_vertice("A", [("B", 5), ("C", 2)])
        self.assertEqual(v.lower_cost_link(), v.lower_cost_link())

    # ---------- vértice sin enlaces ----------
    def test_15_sin_enlaces_no_lanza_error_interno(self):
        """
        Qué debe pasar con un vértice sin enlaces es decisión tuya.
        Aquí se acepta devolver None o lanzar ValueError (ajústalo a tu diseño);
        lo que NO se acepta es un error accidental (UnboundLocalError, etc.).
        """
        v = crear_vertice("A")
        try:
            resultado = v.lower_cost_link()
        except ValueError:
            return  # diseño válido: lanzar ValueError
        self.assertIsNone(resultado)  # diseño válido: devolver None


# ======================================================================
# Reporte personalizado: tipo de error + archivo + línea + código
# ======================================================================
class ReporteResult(unittest.TestResult):

    def __init__(self):
        super().__init__()
        self.resumen = []  # (estado, nombre)

    @staticmethod
    def _nombre(test):
        return test._testMethodName

    @staticmethod
    def _frames_utiles(tb):
        """Frames del traceback, sin el interior de unittest."""
        frames = traceback.extract_tb(tb)
        return [f for f in frames if "unittest" + os.sep not in f.filename]

    def _imprimir(self, etiqueta, test, err):
        tipo, valor, tb = err
        print(f"\n[{etiqueta}] {self._nombre(test)}")
        print(f"   Tipo de error : {tipo.__name__}")
        print(f"   Mensaje       : {valor}")
        print("   Traza (de afuera hacia adentro):")
        for f in self._frames_utiles(tb):
            archivo = os.path.relpath(f.filename, RAIZ)
            print(f"     -> {archivo}, línea {f.lineno}, en {f.name}()")
            print(f"        {f.line}")

    def addSuccess(self, test):
        super().addSuccess(test)
        self.resumen.append(("OK", self._nombre(test)))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.resumen.append(("FALLO", self._nombre(test)))
        self._imprimir("FALLO (assert no cumplido)", test, err)

    def addError(self, test, err):
        super().addError(test, err)
        self.resumen.append(("ERROR", self._nombre(test)))
        self._imprimir("ERROR (excepción inesperada)", test, err)


def main():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestLowerCostLink)
    resultado = ReporteResult()
    suite.run(resultado)

    print("\n" + "=" * 60)
    print("RESUMEN")
    print("=" * 60)
    for estado, nombre in resultado.resumen:
        print(f"  {estado:<6} {nombre}")
    ok = sum(1 for e, _ in resultado.resumen if e == "OK")
    print(f"\n  {ok}/{resultado.testsRun} pruebas pasaron")
    sys.exit(0 if resultado.wasSuccessful() else 1)


if __name__ == "__main__":
    main()