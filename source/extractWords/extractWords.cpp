#include <fstream>
#include <string>
#include <iterator>
#include <map>
#include <string.h>
#include <iostream>
#include <stdlib.h>
using namespace std;
template <class T >
int ahmadyousefan_bSearch(T *array,T & item,int first,int last){
    int retVal1=-1,mean=(first+last)/2;
    T *pmean=array+mean;
    if((array[first]<item)&&(array[last]>item))
        while(first<last){
            if(*pmean==item)    {retVal1=mean;break;}
            if(*pmean<item)     first=mean+1;
            else                last =mean-1 ;
            mean=(first+last)/2;pmean=array+mean;
        }
    if(retVal1<0)
        if(array[first]==item)      retVal1=first;
        else if(array[last]==item)  retVal1=last ;
    return retVal1;
}
class myInt{
      int i1;
   public :
      myInt() { i1=0; }
      myInt(int arg1){i1=arg1;}
      myInt(myInt & arg1){i1=arg1.i1;}
      operator int() const {return i1;}
      friend ostream & operator<<(ostream & out , myInt &arg1);
};
ostream & operator<<(ostream & out , myInt &arg1){return out <<arg1.i1;}
void criticalError(string functionName,string errorStr,string otherReport=""){
    cout <<"program error :::in function"<<functionName<<endl;
    cout<<errorStr<<endl;cout<<otherReport<<endl;
    cout <<"abnormal program termination ::: ahmad yousefan "<<endl;
    exit(0);
}
class delRep{
   map<string,myInt> mapWordsFreq; // farsi words and number of repeation
    string     *arrayOfPreWords;
    int         *arrayOfFreq;
   ifstream inpFile ;
   int numberOfPreWords;
  public:
    delRep(string,string);
    void run(void);
    void saveAll(string,string);
    ~delRep(void){inpFile.close();}
};
delRep::delRep(string inputFileName,string preWordsFileName){
    inpFile.open(inputFileName.c_str());
    if(!inpFile)
        criticalError( "delRep::delRep  3","can not open input File Name ",inputFileName);
    ifstream file1(preWordsFileName.c_str());
    if(!file1)
        criticalError("delRep::delRep   7 "," can not open input preWords File Name ",preWordsFileName);
    int i1,i2=0; file1>>i1; file1>>i1; i1++;string str1;
    arrayOfPreWords=new string[i1+2];
    arrayOfFreq    =new int[i1+2];
    for(int j=0;j<=i1;j++)	arrayOfFreq[j]=0;
    file1>>str1;
    while(!file1.eof()){
        arrayOfPreWords[i2++]=str1;
        file1>>str1;
        if(i2>i1)
            criticalError("delRep::delRep 15","previous word length uncorrect ");
    }
    numberOfPreWords=--i2; file1.close();
}
void delRep::run(void){
   int i=0,j=0;string str1; inpFile >>str1;
   while(!inpFile.eof())   {
        i=ahmadyousefan_bSearch(arrayOfPreWords,str1,0,numberOfPreWords);
        if(i>-1) arrayOfFreq[i]  +=1;
        else        mapWordsFreq[str1]=mapWordsFreq[str1]+1;
	inpFile >>str1;
    }
}
void delRep::saveAll(string wordsFileName,string freqFileName){
    int i,j=0,k=0;
    ofstream wordsFile(wordsFileName.c_str());
    if(!wordsFile)
        criticalError("delRep::saveAll","can not open output file name ",wordsFileName);
    ofstream freqFile(freqFileName.c_str());
    if(!freqFile)
        criticalError("delRep::saveAll","can not open freq  file name ",freqFileName);
     for(i=0;i<=numberOfPreWords;i++)
        if(arrayOfFreq[i]>0){
            wordsFile<<arrayOfPreWords[i]<<endl;
            freqFile <<arrayOfFreq[i]    <<endl;
	    k++;
        }
        else j++;
   map<string,myInt>::iterator iter1;
   map<string,myInt>::iterator pEndSet;
   iter1  =mapWordsFreq.begin();
   pEndSet=mapWordsFreq.end();
   for(;iter1 != pEndSet;iter1++){
        wordsFile<<iter1->first <<endl;
        freqFile <<iter1->second<<endl;
   }
    wordsFile.close();freqFile .close();
    cout<<" number of not correct  previous words "<<j<<endl;
    cout<<"number of correct is :::"<<k<<endl;
    cout<<"number if Previous words is :::"<<numberOfPreWords<<endl;
}
int  main(void){
 string path="/home/yousefan/thesis/dataset/";
 string inputWordsFileName=path+"words1256.hh";
 string preWordsFileName  =path+"allPreparedWords.hh";
 path   += "out1/";
 string wordsFile=path+"allWords.hh";
 string freqFile =path+"FreqWords.hh";
 delRep r1(inputWordsFileName,preWordsFileName);
  r1.run();
  r1.saveAll(wordsFile,freqFile);
  cout<<"normally end  :::: ahmad yousefan message "<<endl; return 0;
}
