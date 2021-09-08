#include<stdio.h>


int bins_left(int *arr,int n,int t){

	int l = 0,r = n-1;

	int m = 0;

	int res = -1;

	while(l<=r){

		m = r-(r-l)/2;

		if(arr[m]==t){

			res = m;

			r = m - 1;

		}

		else if(arr[m]<t){

			l = m + 1;
		}
		else{


			r = m - 1;
		}

	}

	return -1;


}

int bins_right(int *arr,int n,int t){

	int l = 0,r = n-1;

	int m = 0;

	int res = -1;

	while(l<=r){

		m = r-(r-l)/2;

		if(arr[m]==t){

			res = m;

			l = m+1;

		}

		if(arr[m]<t){
			l = m + 1;
		}
		else{
			r = m - 1;
		}

	}

	return res;

}


int main(int argc, char const *argv[])
{
	
	int arr[] = {1,2,2,3,3,5,5,5,25,75,75,75,97,97,97};

	

	return 0;
}

