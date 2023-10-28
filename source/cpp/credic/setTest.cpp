//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------
#include <set>
#include <fstream>
#include <string>
#include <iterators>
using namespace std;
#pragma argsused

char *pAllFiles;
string tempStr1="";
char tempChars1[100];
bool getNextWord(void)
{
   int i=0;
   if(!*pAllFiles)
      return false;
   while(*pAllFiles==' ')
      pAllFiles++;
   if(!*pAllFiles)
      return false;
   while(*pAllFiles != ' ')
         tempChars1[i++]=*pAllFiles++;
   tempChars1[i]='\0';
   tempStr1=tempChars1;
   return true;
}
int main(void)
 {
   int i1;
   char path00[]= "e:\\yousefan\\tez\\dataset\\";
   FILE  *inFile;
   char name[100];
   strcpy(name,path00);strcat(name,"sampleW2.hl");
   if((inFile=fopen(name,"r"))==NULL)
   {
       cout<<"\n    aa can not open input File ";
       cin>>i1;
       return 1;
   }
   strcpy(name,path00);strcat(name,"allWords.htm");
   ofstream outFile(name);
   if(!outFile)
   {
       cout<<"\ncan not open output File ";
       cin >>i1;
       return 1;
   }
   char headStr1[]="<html><head><meta HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; charset=windows-1256\"></head><body bgcolor=\"white\" dir=\"ltr\"><p style=\"font-size:14pt;\" align=\"right\">\n";
   outFile<<headStr1;
   fseek(inFile,0,SEEK_END);
   long int len1=ftell(inFile);
   fseek(inFile,0,SEEK_SET);
   char *allFiles=new char[len1+4];
   fread(allFiles,len1,1,inFile);
   allFiles[len1]=allFiles[len1+1]='\0';
   pAllFiles=allFiles;
   set<string> setOfWords;
   while(getNextWord())
   {
      setOfWords.insert(tempStr1);
//      cout<<tempStr1<<endl;
   }
   set<string>::iterator a1i=setOfWords.begin();
   set<string>::iterator endSet=setOfWords.end();
   for(;a1i != endSet;a1i++)
      outFile<<*a1i<<" ";
   strcpy(headStr1,"\n</body></html>\n");
   outFile<<headStr1;
   outFile.close();
   fclose(inFile);
cin >>i1;
return 0;
 }
//---------------------------------------------------------------------------
