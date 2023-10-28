//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------
#include <fstream>
#include <string>
#include <iterators>
#include <map>
#include <string.h>
#define Uchar unsigned char
using namespace std;

#pragma argsused


/*
   in this program read all htmls and delete all other than farsi
   then delete repeated word and remove extra ZWNJ and kasre
   i need to change this file so that can save files in one file
   and repetition of it with name
   this program use the file that creat with python (name of all htmls)
   use cp1256 code for farsi (utf-8 and other code was added

*/



class myInt{
      int i1;
   public :
      myInt(){i1=0;}
      myInt(int arg1){i1=arg1;}
      myInt(myInt & arg1){i1=arg1.i1;}

      operator int() const {return i1;}
      friend ostream & operator<<(ostream & out , myInt &arg1);
};
ostream & operator<<(ostream & out , myInt &arg1)
{ return out <<arg1.i1;}

class delRep{
    char *pCurFile;//current open html file for find farsi words (loaded in character array)
    string tempStr1;// current farsi word in string form
    char tempChars1[500];//current farsi word in array of characters form
    map<string,myInt> setOfWords; // farsi words and number of repeation
    Uchar *plFarsi;
    char *allWords ;
    char *htmlFile ;  //name of current html file
    Uchar lFarsi[200];//list of farsi characters in cp1256
    int maxFileLen;  //maximum file length

    bool getNextWord(void); // get next word from current html file
    void delUnFarsi();
  public:
    delRep();
    void run(char *chars1,char *words,int max1);
    void saveAll(char *path);
};

bool delRep::getNextWord(void)
{ // get next word from current html file
   int i=0;
   if(!*pCurFile)   return false;
   while(*pCurFile==' ')    pCurFile++;
   if(!*pCurFile)   return false; // check if end of file recieved
   while((*pCurFile != ' ') && (*pCurFile))
         tempChars1[i++]=*pCurFile++;
   Uchar ch1=allWords[i-1];
   /// the following code added
   if(ch1==0x9d)  // del ZWNJ (Zero Width Non-Joiner)
      i--;
   ch1=allWords[i-1];
   if(ch1==0xf6)  // del kasre (zir no zebar)
    i--;
   ch1=allWords[i-1];
   if(ch1==0x9d) // del ZWNJ (Zero Width Non-Joiner)
    i--;
   tempChars1[i]='\0';
   tempStr1=tempChars1;
   return true;
}

void delRep::delUnFarsi()
{
   int j=0;Uchar ch1;bool preIsSpace=false;
   char *pAllFile=htmlFile;
   while((ch1=*pAllFile++)!=NULL)
       if(ch1<=128)
          if(!preIsSpace)
          {allWords[j++]=' ';preIsSpace=true;}
       else{
          plFarsi=lFarsi;
          while((ch1>*plFarsi)&& (*plFarsi))
            plFarsi++;
          if(ch1==*plFarsi){
             allWords[j++]=ch1;
             preIsSpace=false;
          }
          else if(!preIsSpace)
          {allWords[j++]=' ';preIsSpace=true;}
       }
   allWords[j++]=' ';
   allWords[j++]='\0';
}


delRep::delRep(){
  Uchar lFarsi22[]={0x81,0x8d,0x8e,0x90,0x9d,0xc1,0xc2,0xc3,0xc4,0xc5,0xc6,
    0xc7,0xc8,0xc9,0xca,0xcb,0xcc,0xcd,0xce,0xcf,0xd0,0xd1,0xd2,0xd3,0xd4,
    0xd5,0xd6,0xd8,0xd9,0xda,0xdb,0xdd,0xde,0xdf,0xe1,0xe3,0xe4,0xe5,0xe6,
    0xec,0xed,0xf0,0xf1,0xf2,0xf3,0xf5,0xf6,0xf8,0xfa
  };
  int i;
  for(i=0;lFarsi22[i];i++)
    lFarsi[i]=lFarsi22[i];
  lFarsi[i]=lFarsi22[i];
  plFarsi=lFarsi;
  maxFileLen=800000;
  allWords = new char[maxFileLen+4];
  htmlFile = new char[maxFileLen+4];
  allWords[0]=htmlFile[0]='\0';
}
void delRep::run(char *chars1,char * allWordsInFile,int maxWordsLength)
{
   ifstream fHtml(chars1);
   fHtml.seekg(0,ios::end);
   int fileLen=fHtml.tellg();
   fHtml.seekg(0,ios::beg);
   if(fileLen<maxFileLen)
      fHtml.read(htmlFile,fileLen);
   else
      cout<<"error in reading big file "<<chars1<<endl;
   fHtml.close();
   htmlFile[fileLen]='\0';
   delUnFarsi();
   pCurFile=allWords;
   int i=0;
   while(getNextWord())
   {
      if(!i)
        strcpy(allWordsInFile,tempChars1);
      else if (i>maxWordsLength-30)
      {
        cout<<"error in file Length in delRep::run(...) in file "<<endl;
        cout<<chars1<<endl<<endl<<endl;
        break;
      }
      else
        strcat(allWordsInFile,tempChars1);
      i+=strlen(tempChars1);
      setOfWords[tempStr1]=setOfWords[tempStr1]+1;
   }
}

void delRep::saveAll(char *path)
{
   char allWordsFileName[]="allWords.html";
   char deletedWordsFileName[]="deletedWords.html";
   char allWordsFileNameTxt[]="allWords.h1";
   char deletedWordsFileNameTxt[]="delWords.h1";
   char numberOfWordsFileNameTxt[]="noWords.h1";

   char name[300];
   strcpy(name,path);strcat(name,allWordsFileName);
   ofstream fileAllWords(name);
   strcpy(name,path);strcat(name,deletedWordsFileName);
   ofstream fileDeletedWords(name);

   strcpy(name,path);strcat(name,allWordsFileNameTxt);
   ofstream fileAllWordsTxt(name);
   strcpy(name,path);strcat(name,deletedWordsFileNameTxt);
   ofstream fileDeletedWordsTxt(name);
   strcpy(name,path);strcat(name,numberOfWordsFileNameTxt);
   ofstream fileNumberOfWordsTxt(name);
   char headStr1[400];
   strcpy(headStr1,"<html><head><meta HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; charset=windows-1256\">");
   strcat(headStr1,"</head><body bgcolor=\"white\" dir=\"ltr\"><p style=\"font-size:14pt;\" align=\"right\">\n");
   fileAllWords<<headStr1;
   fileDeletedWords<<headStr1;
   map<string,myInt>::iterator iter1;
   map<string,myInt>::iterator pEndSet;
   iter1=setOfWords.begin();
   pEndSet=setOfWords.end();
   for(;iter1 != pEndSet;iter1++)
     if(iter1->second <2){
        fileDeletedWords<<iter1->first<<' '<<iter1->second<<"<br>"<<endl;
        fileDeletedWordsTxt<<iter1->first<<' ';
     }
     else{
       fileAllWords<<iter1->first<<' '<<iter1->second<<"<br>"<<endl;
       fileAllWordsTxt<<iter1->first<<' ';
       fileNumberOfWordsTxt<<iter1->second;
     }
   strcpy(headStr1,"\n</body></html>\n");
   fileAllWords<<headStr1;
   fileDeletedWords<<headStr1;
   fileAllWords.close();
   fileDeletedWords.close();
   fileAllWordsTxt.close();
   fileDeletedWordsTxt.close();
   fileNumberOfWordsTxt.close();
}


void main(void){
 delRep r1;int i=0;
 char chars1[1024];
 const int maxWordsLength=65000;
 char wordsOfFile[maxWordsLength];
 ifstream fileNameOfHtmls("e:\\yousefan\\ahmad\\Htm1s256.hh");
 ofstream fileOfAllWords("e:\\yousefan\\tez\\fileOfAllWords.h1");
 fileNameOfHtmls.getline(chars1,1022);
 while(!fileNameOfHtmls.eof()){
   r1.run(chars1,wordsOfFile,maxWordsLength);
   fileOfAllWords<<wordsOfFile<<endl;
   fileNameOfHtmls.getline(chars1,1022);
   i++;
   if(i%10000 ==0)
        cout<<i<<endl;
 }
 fileNameOfHtmls.close();
 fileOfAllWords.close(); 
 char path[]="e:\\yousefan\\tez\\";
 r1.saveAll(path);
 cout<<"THE END "<<i<<endl;char chch1[10];cin>>chch1;
}
//---------------------------------------------------------------------------

