st=>start: Inicio
e=>end: Fin
op1=>operation: Imprimir bienvenida
op2=>operation: Mostrar menú
op3=>operation: Llamar a agregar_registro()
op4=>operation: Llamar a buscar_persona()
op5=>operation: Llamar a borrar_registro()
op6=>operation: Imprimir mensaje despedida
cond1=>condition: ¿Opción 1 seleccionada?
cond2=>condition: ¿Opción 2 seleccionada?
cond3=>condition: ¿Opción 3 seleccionada?
cond4=>condition: ¿Opción 4 seleccionada?
op7=>operation: Imprimir opción inválida

st->op1->op2
op2->cond1
cond1(yes)->op3->op2
cond1(no)->cond2
cond2(yes)->op4->op2
cond2(no)->cond3
cond3(yes)->op5->op2
cond3(no)->cond4
cond4(yes)->op6->e
cond4(no)->op7->op2
