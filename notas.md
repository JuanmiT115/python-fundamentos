# Notas Fundamentos Python

## Semana 0, Funciones (Functions)
- ¿Qué es una variable?
  - Es un espacio de memoria en donde se puede guardar información y tienen un nombre el cual me permite acceder a ellas con este mismo.

- ¿Que hace input() y print()?
  - Input permite recibir información por parte del usuario y print lo que hace es mostrar lo que pidamos en la pantalla.
  - *Aclaración:* input siempre devuelve un valor de texto (str).

- ¿Qué es f-string?
  - Es una forma que nos permite poner dentro de {} variables y en este caso dentro de un print las imprima sin ninguna problema dentro de "".
  - Tambien permite dar formato:<br/>
  
  ```python
        total = 15.678
        print(f"Total: {total:.2f}") #Total: 15.68

  ```

- ¿Para qué sirven .strip() y .title()?
  - El .strip funciona para eliminar los espacios en blanco tanto al inicio como al final de una cadena de texto y .title lo que hace poner en mayúsculas la primera letra de cada palabra.