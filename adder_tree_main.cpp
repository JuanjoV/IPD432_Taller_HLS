
#include "adder_tree_main.hpp"

/* Función TOP */
void adder_tree_main(res_data_t *result, data_t x[N], data_t y[N])
{
    //#pragma HLS INTERFACE port=x mode=ap_memory 
    //#pragma HLS INTERFACE port=y mode=ap_memory
    //#pragma HLS INTERFACE port=result mode=ap_none

    //#pragma HLS ARRAY_PARTITION variable=x dim=1 type=complete
    //#pragma HLS ARRAY_PARTITION variable=y dim=1 type=complete

    res_data_t temp = 0;
    /* Loop principal. Recomendado etiquetarlos siempre. */
	SIMPLE_LOOP : for (int i = 0; i < N; ++i)
    {
        //#pragma HLS PIPELINE II=2
        //#pragma HLS UNROLL
		temp += x[i] + y[i];
	}

    *result = temp;

}