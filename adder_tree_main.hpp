/* Evita inclusion recursiva */
#pragma once /* NO CONFUNDIR CON PRAGMAS HLS. */

/* Contiene el tipo de dato de enteros de precision arbitraria */
#include "ap_int.h"

/* Tamano de cada vector */
#define N 5
/* Ancho de bits  */
#define BITSIZE 15


/* Tipo de dato para entradas */
typedef ap_int<BITSIZE> data_t;
/* Tipo de datos para salidas */
typedef ap_int<BITSIZE> res_data_t;

/* Declaracion de funcion top */
void adder_tree_main(res_data_t *result, data_t x[N], data_t y[N]);