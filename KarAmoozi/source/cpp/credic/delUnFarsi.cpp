//---------------------------------------------------------------------------

#pragma hdrstop
#include<stdio.h>
#include<string.h>
#define Uchar unsigned char
//---------------------------------------------------------------------------
#pragma argsused
class delUnFarsi{
int main(int argc, char* argv[])
{
   Uchar lFarsi[]={0x81,0x8d,0x8e,0x90,0x9d,0xc1,0xc2,0xc3,0xc4,0xc5,0xc6,
   0xc7,0xc8,0xc9,0xca,0xcb,0xcc,0xcd,0xce,0xcf,0xd0,0xd1,0xd2,0xd3,0xd4,
   0xd5,0xd6,0xd8,0xd9,0xda,0xdb,0xdd,0xde,0xdf,0xe1,0xe3,0xe4,0xe5,0xe6,
   0xec,0xed,0xf0,0xf1,0xf2,0xf3,0xf5,0xf6,0xf8,0xfa};
   Uchar path00[]= "e:\\yousefan\\tez\\dataset\\";
   FILE  *inFile,*outFile;
   Uchar name[100];
   name[0]='\0';
   strcat(name,path00);strcat(name,"fileOfAllHtmls.hh");
   if((inFile=fopen(name,"r"))==NULL)
   {
       printf("\ncan not open input File ");
       return 1;
   }
   name[0]='\0';
   strcat(name,path00);strcat(name,"sampleWords2.hl");
   if((outFile=fopen(name,"w"))==NULL)
   {
       printf("\ncan not open output File ");
       return 1;
   }
   Uchar headStr1[]="<html><head><meta HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; charset=windows-1256\"></head><body bgcolor=\"white\" dir=\"ltr\"><p style=\"font-size:14pt;\" align=\"right\">\n";
//   fwrite(headStr1,strlen(headStr1)+1,1,outFile);
   int i=0,j=0;
   Uchar ch1=' ',*plFarsi;
   bool preIsSpace=false;
   fseek(inFile,0,SEEK_END);
   long int len1=ftell(inFile);
   fseek(inFile,0,SEEK_SET);
   char *allFiles=new char[len1];
   char *allWords=new char[len1];
   fread(allFiles,len1-4,1,inFile);
   Uchar *pAllFiles;
   pAllFiles=allFiles;
   j=0;
   len1-=10;
   for(i=0;i<len1;i++)
   {
         ch1=*pAllFiles++;
         if(ch1<=128)
         {
            if(!preIsSpace)
            {
               allWords[j]=' ';
               preIsSpace=true;
               j++;
            }
         }
         else
         {
            plFarsi=lFarsi;
            while(ch1>*plFarsi)
               plFarsi++;
            if(ch1==*plFarsi)
            {
               allWords[j]=ch1;
               j++;
               preIsSpace=false;
            }
            else if(!preIsSpace)
            {
                  allWords[j++]=' ';
                  preIsSpace=true;
            }

         }
      }

  allWords[j++]=' ';
  allWords[j++]='\0';
  fwrite(allWords,strlen(allWords)+1,1,outFile);

/*

//////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////
   name[0]='\0';
   strcat(name,path00);strcat(name,"sampleWords2.htm");
   FILE *outFile2;
   if((outFile2=fopen(name,"w"))==NULL)
   {
       printf("\ncan not open output File ");
       return 1;
   }
   fwrite(headStr1,strlen(headStr1)+1,1,outFile2);
   fwrite(allFiles,strlen(allWords)+1,1,outFile2);
   strcpy(headStr1,"??????????????????????????????????????????????????/");
   fwrite(headStr1,strlen(headStr1)+1,1,outFile2);
   fwrite(allWords,strlen(allWords)+1,1,outFile2);

//////////////////////////////////////////////////////////////////////

  */
   strcpy(headStr1,"\n</body></html>\n");
//   fwrite(headStr1,strlen(headStr1)+1,1,outFile);
   fclose(outFile);fclose(inFile);

/*
//////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////
   fwrite(headStr1,strlen(headStr1)+1,1,outFile2);fclose(outFile2);
//////////////////////////////////////////////////////////////////////
  */
   scanf("%d",&i);
   return 0;
}

//---------------------------------------------------------------------------
