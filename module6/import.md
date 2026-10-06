# Formas de importar en Python

## 1. `import modulo`

Importa el modulo completo y se accede a sus nombres mediante el prefijo del modulo.

En [ft_alembic_0.py](ft_alembic_0.py#L1-L7):

```python
import elements

elements.create_fire()
```

Tambien aparece en:

## 2. `from modulo import nombre`

Importa directamente una funcion, clase o variable. Despues se usa sin el prefijo del modulo.

En [ft_alembic_1.py](ft_alembic_1.py#L1-L7):

```python
from elements import create_water

create_water()
```

## 3. `import paquete.modulo`

Importa un modulo usando su ruta completa.

En [ft_alembic_2.py](ft_alembic_2.py#L1-L7):

```python
import alchemy.elements

alchemy.elements.create_earth()
```

## 4. `import paquete`

Importa el paquete y permite acceder a los nombres que el paquete expone.

En [ft_alembic_4.py](ft_alembic_4.py#L1-L12):

```python
import alchemy

alchemy.create_air()
```

Esto funciona porque [alchemy/__init__.py](alchemy/__init__.py#L2-L5) importa y expone `create_air`.

## 5. Importar desde un paquete

En [ft_alembic_5.py](ft_alembic_5.py#L1-L7):

```python
from alchemy import create_air
```

Esto busca un nombre llamado `create_air` dentro del paquete `alchemy`, normalmente porque esta definido o reexportado desde `alchemy/__init__.py`.

La cadena es:

```python
# alchemy/__init__.py
from alchemy.elements import create_air
```

Por eso despues funciona:

```python
from alchemy import create_air
```

## 6. Importar un submodulo desde un paquete

En [alchemy/transmutation/recipes.py](alchemy/transmutation/recipes.py#L3-L4):

```python
from alchemy import potions

potions.strength_potion()
```

Aqui `potions` es el modulo [alchemy/potions.py](alchemy/potions.py), no una funcion concreta.

Comparacion:

```python
from alchemy import potions
potions.strength_potion()
```

frente a:

```python
from alchemy.potions import strength_potion
strength_potion()
```

## 7. Import relativo con un punto

Un punto significa "desde el paquete actual".

En [alchemy/grimoire/dark_spellbook.py](alchemy/grimoire/dark_spellbook.py#L1-L2):

```python
from .dark_validator import validate_ingredients
```

El punto representa `alchemy.grimoire`.

## 8. Import relativo con dos puntos

En [alchemy/transmutation/recipes.py](alchemy/transmutation/recipes.py#L1-L2):

```python
from ..elements import create_air
```

Los dos puntos suben un nivel:

```text
alchemy.transmutation.recipes
                  ..
alchemy.elements
```

Por tanto, importa `create_air` desde [alchemy/elements.py](alchemy/elements.py).

Regla:

```text
.       paquete actual
..      paquete padre
...     dos niveles hacia arriba
```

## 9. Alias con `as`

En [alchemy/__init__.py](alchemy/__init__.py#L3-L4):

```python
from alchemy.potions import healing_potion as heal
```

La funcion original se llama `healing_potion`, pero dentro del archivo queda disponible como `heal`:

```python
heal()
```

## 10. Importar varios nombres en una linea

En [alchemy/potions.py](alchemy/potions.py#L1-L3):

```python
from alchemy.elements import create_air, create_earth
```

Importa dos funciones:

```python
create_air()
create_earth()
```

## 11. Import dentro de una funcion

En [alchemy/grimoire/light_spellbook.py](alchemy/grimoire/light_spellbook.py#L5-L9):

```python
def light_spell_record(...):
    from .light_validator import validate_ingredients
```

Este import no se ejecuta al cargar el modulo, sino cuando se llama a `light_spell_record`.

Aqui tiene una finalidad importante: evitar una importacion circular entre:

```text
light_spellbook.py
    -> light_validator.py
        -> light_spellbook.py
```

El modulo oscuro no aplica esta tecnica. [dark_spellbook.py](alchemy/grimoire/dark_spellbook.py#L1-L2) y [dark_validator.py](alchemy/grimoire/dark_validator.py#L1-L2) se importan mutuamente al cargar los archivos, provocando el error indicado en [ft_kaboom_1.py](ft_kaboom_1.py#L5-L8).
