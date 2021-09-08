#include<stdio.h>
#include<math.h>
#define min(x,y) (x>y?y:x)

int linear_search(int *arr,int n,int t){

	for(int i = 0 ; i < n ; i++){
		if(arr[i]==t){
			return i;
		}
	}

	return -1;
}

int binary_search(int *arr,int n,int t){

	int l = 0,r = n-1;

	int m = 0;

	while(l<=r){

		m = r-(r-l)/2;

		if(arr[m]==t){
			return m;
		}
		if(arr[m]<t){
			l = m + 1;
		}
		else{
			r = m - 1;
		}

	}

	return -1;

}

int jump_search(int arr[],int n,int t){

  int prev = 0;

  int step = sqrt(n);

  while(arr[min(step,n)-1]<t){

    prev = step;

    step+=sqrt(n);

    if(prev>=n){
      return  -1;
    }

  }

  while( prev<min(n,step)){

    if(arr[prev++]==t){
      return prev-1;
    }
  }
  return -1;

}

int main(int argc, char const *argv[])
{

  int arr[] = {1,2,3,4,5,5};
  
  printf("%d",jump_search(arr, 6, 5));

	return 0;
}
