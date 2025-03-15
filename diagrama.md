```mermaid
flowchart TD
    A[Inicio] --> B[Imprimir bienvenida]
    B --> C[Mostrar menú]
    C --> D{¿Opción seleccionada?}
    D -->|Opción 1| E[Agregar registro]
    E --> C
    D -->|Opción 2| F[Buscar persona]
    F --> C
    D -->|Opción 3| G[Borrar registro]
    G --> C
    D -->|Opción 4| H[Imprimir mensaje despedida]
    H --> I[Fin]
    D -->|Opción inválida| J[Imprimir opción inválida]
    J --> C
