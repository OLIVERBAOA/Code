/*************************************************************************
    > File Name: fork01.cpp
    > Author: Royecode
    > Mail: Royecode@163.com 
    > Created Time: 2015年10月11日 星期日 21时03分07秒
 ************************************************************************/

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main(void)
{
   int i;
   for(i=0; i<2; i++){
      fork();
      //printf("-");
	  puts("-");
   }

   wait(NULL);
   wait(NULL);

   return 0;
}
