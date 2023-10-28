//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------
#include <fstream>
#include <string>
#include <iterators>
#include <list>
#include <string.h>

#pragma argsused
class stemCls{
   char  **allWordsArray;
   int   *reverseOrder;
   int   numberOfWords;

   void stemCls(void){
      char *lineWords;
      ifstream f1("e:\\yousefan\\cw.hh");
      f1.seekg(0,ios::end);
      int len1=f1.tellg();
      f1.seekg(0,ios::beg);
      lineWords=new char[len1+2];
      f1.read(lineWords,len1);
      f1.close();
      lineWords[len1]=lineWords[len1+1]='\0';
      char word1[1024];
      int i=0;
      char *tempWord;
      char *pLine1=lineWords;
      for(pLine1=lineWords,numberOfWords=0;*pLine1;pLine1++){
         if(*pLine1==' ')  numberOfWords++;
      allWordsArray=new char *[numberOfWords];
      int noCur=0;
      for(pLine1=lineWords,i=0;*pLine1,pLine1++){
         if(*pLine1==' '){
            word1[i++]='\0';
            allWordsArray[noCur]=new char[i];
            strcpy(allWordsArray[noCur],word1);
            noCur++;i=0;pLine1++;
         }
         else
            word1[i++]=*pLine1;

   }
};
int main(int argc, char* argv[])
{
        return 0;
}
//---------------------------------------------------------------------------
