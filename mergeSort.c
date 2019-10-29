#include <stdio.h>
#include <stdlib.h>

typedef int DATA_TYPE;

enum sym {
	greater,
	less,
	equal
};



int compare(DATA_TYPE* val1, DATA_TYPE* val2);
DATA_TYPE* mergeSort(DATA_TYPE ary[], int start, int end);

int main()
{

	DATA_TYPE aryX[11] = {6 ,2,3,4,1,2,3,4,0,-9,9};

	DATA_TYPE* arySorted = mergeSort(aryX, 0,10 );

	printf("\n");
	for(int i=0; i<11; i++)
	{
		printf("%d ", arySorted[i]);
	}

}

int compare(DATA_TYPE* val1, DATA_TYPE* val2)
{
	if(*val2 < *val1)
	{
		return greater;
	} else if(*val2 == *val1){
		return equal;
	} else {
		return less;
	}
}

DATA_TYPE* mergeSort(DATA_TYPE ary[], int start, int end)
{
	int mid = ((end - start) / 2) + start;
	//printf("\nSplitting - %d %d %d\n", start, mid,end);

	if(end <= start)
	{
		//printf("\nDirect Merging - %d %d %d\n", start, mid,end);
		DATA_TYPE* newAry = (DATA_TYPE*)malloc(sizeof(DATA_TYPE));
		newAry[0] = ary[start];
		//printf("\n%d ",newAry[0]);
		return newAry;
	}

	DATA_TYPE* ary1 = (DATA_TYPE*)mergeSort(ary, start, mid);
	DATA_TYPE* ary2 = (DATA_TYPE*)mergeSort(ary, mid+1, end);

	int size_1 = mid - start + 1;
	int size_2 = end - (mid+1) + 1;

	int min_size = 0;

	if(size_1 <= size_2)
	{
		min_size = size_1;
	}
	else
	{
		min_size =size_2;
	}

	DATA_TYPE* newAry = (DATA_TYPE*)malloc(sizeof(DATA_TYPE)*(end - start + 1));

	int j = 0;
	int i = 0;
	int k = 0;
	//printf("\nMerging - %d %d %d\n", start, mid,end);
	//printf("\nsize - %d %d %d\n", size_1, size_2, min_size);
	while( i < size_1 && j < size_2)
	{
		if(compare(&ary1[i] , &ary2[j]) == less)
		{
			newAry[k] = ary1[i];
			//printf("\ni - %d",newAry[k]);
			i++;
			k++;
		} else if (compare(&ary1[i] , &ary2[j]) == greater){
			newAry[k] = ary2[j];
			//printf("\nj - %d",newAry[k]);
			j++;
			k++;
		} else {
			newAry[k] = ary1[i];
			//printf("\nij - %d",newAry[k]);
			i++;
			k++;
			newAry[k] = ary2[j];
			//printf("\nij - %d",newAry[k]);
			j++;
			k++;
		}
	}


	for(; i<size_1; k++)
	{
		newAry[k] = ary1[i];
		//printf("\nr1 - %d",newAry[k]);
		i++;
	}

	for(; j<size_2; k++)
	{
		newAry[k] = ary2[j];
		//printf("\nr2 - %d",newAry[k]);
		j++;
	}		


	return newAry;
}
