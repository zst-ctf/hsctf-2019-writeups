#include <stdio.h> 
#include <stdlib.h> 
#include <stdint.h> 
#include <time.h> 

int main(void) { 
	// Use current time as seed for random generator 
	srand(time(0)); 

	uint32_t local_268[6];
	local_268[0] = 0x79;
	local_268[1] = 0x12c97f;
	local_268[2] = 0x135f0f8;
	local_268[3] = 0x74acbc6;
	local_268[4] = 0x56c614e;
	local_268[5] = 0xffffffe2;

	// subtract a random no. from 1 to 10 inclusive.
	for (int i = 0; i < 6; i++) {
		local_268[i] -= (rand() % 10 + -1);
	}

	// Sum up all numbers
	int local_288 = 0;
	for (int i = 0; i < 6; i++) {
		local_288 += local_268[i];
	}

	printf("%d\n", local_288);
} 