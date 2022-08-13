# Desafio-Back-end
Hecho en Python 3.9.13, utilizando sqlite3. No requiere previa instalación, ni bibliotecas externas.

Programa que proporciona la posibilidad de crear boletas de servicios, pagarlas y filtrarlas.

Forma de uso:
# Todas las opciones elegibles son mediante los numeros especificados en los menús interactivos
#Para Crear una Boleta se deberá presionar '1' en el menu principal y se procedera a pedir los datos para la misma
      -Seleccionar el servicio al cual se creara la boleta. Entre 1 y 3.
      -Introducir una descripcion
      -Introducir una Fecha de Vencimiento, que deberá estar en formato YYYY-MM-DD. Ej: 2022-09-12
      -Introducir un Importe, el cual debe ser un numero.
      -Seleccionar el estado de la boleta. Entre 1 y 2.
      -Introducir el codigo de barra, que puede contener letras y numeros. Pero debe ser unico e irrepetible.

#Para ejecutar un pago de una boleta ya creada:
      -Seleccionar la forma de pago. Entre 1 y 3.
      -SI la forma de pago es tarjeta de credito o tarjeta de debito. Introducir el numero de la tarjeta, de lo contrario continuar al paso siguiente.
      -Ingresar el codigo de barra de la boleta a pagar. Debe ser un codigo de una boleta ya existente.
      -Al completar estos pasos, automaticamente se guardara la fecha actual de ese pago y el estado de la boleta pasara a ser 'Pagado'.
      
 #Para ver las boletas:
      -Seleccionar el estado de las boletas que desea ver entre las opciones 2 a 4, o bien seleccionar 1 para ver todos los estados.
      -Seleccionar el servicio que desea ver entre las opciones 2 a 4, o bien seleecione 1 para ver todos los servicios.
      -A continuación verá el Servicio (solo si este no fue especificado al momento de filtrar), la fecha de vencimiento, el importe 
      y el codigo de barra de todas las boletas que cumplan con los parametros especificados anteriormente.
 
 #Para filtrar por fecha:
      -Ingresar la fecha inicial para filtrar, en formato YYYY-MM-DD. Ej: 2022-01-01
      -Ingresar la fecha limite para filtrar, en formato YYYY-MM-DD. Ej: 2022-12-12
      -A continuacion verá la fecha de pago, el importe y el codigo de barra de todas aquellas boletas que hayan sido pagadas dentro de los limites temporales
      anteriormente especificados. Acompañado del monto total recaudado y la cantidad total de boletas dentro de esos limites.
      
 #Para finalizar la ejecucion seleccionar la opcion '0' en el menu principal.
      

