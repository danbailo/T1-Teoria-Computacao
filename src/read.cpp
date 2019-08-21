#include <stdio.h>
#include <string.h>
#include <dirent.h>

#include <iostream>
#include <vector>
#include <experimental/filesystem>

using namespace std;
namespace fs = std::experimental::filesystem;

int max(int a, int b) { return (a > b)? a : b; } 

// Returns the maximum value that can be put in a knapsack of capacity W 
int knapSack(int W, vector<int> wt, vector<int> val, int n) { 
	int i, w; 
	int K[n+1][W+1]; 
  
   	// Build table K[][] in bottom up manner 
	for (i = 0; i <= n; i++){ 
		for (w = 0; w <= W; w++) { 
			if (i==0 || w==0) K[i][w] = 0; 
			else if (wt[i-1] <= w) K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]); 
			else K[i][w] = K[i-1][w]; 
		} 
	} 
	return K[n][W]; 
} 

int main() {
	vector<int> prices,weights;
	int state=0;
	int w,n;

	FILE* f=fopen("./entradas/input13.in","r");
	char buff[1024];
	while(fgets(buff,1024,f)){
		if(state==0){
			sscanf(buff,"%i\n",&n);
			state=1;
		}
		else if(state==1){
			int id,lucro,peso;
			sscanf(buff,"    %i %i %i\n",&id,&lucro,&peso);
			prices.push_back(lucro);
			weights.push_back(peso);
			if(id==n) state=2;
		}
		else if(state==2) sscanf(buff,"%i\n",&w);
	}
	// printf("instancia: %s\n",instance.c_str());
	printf("w=%i n=%i\n",w,n);
	printf("\n");
	for(int i=0;i<prices.size();i++){
		printf("[%i] %i %i\n",i,prices[i],weights[i]);
	}
	printf("knapsack: %i\n", knapSack(w, weights, prices, n));
	return 0; 

}