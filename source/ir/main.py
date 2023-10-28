import os,sys,string
import runProgram,stem
if sys.platform =='win32':  path00='g:\\yousefan\\thesis\\work';
else:                                    path00='/home/yousefan/thesis/work';
sourcePath=os.path.join(path00,'source')
dataPath  =os.path.join(path00,'data')
sys.path.append(os.path.join(sourcePath,'python'))
import mapUnicodeCp1256
uniformFunction=mapUnicodeCp1256.uniformUnicodeString
stemObject=stem.stemCls(os.path.join(dataPath,'lastDerivation'),uniformFunction)
stemFunction=stemObject.stem
param1={}
param1['docQueryPath']=os.path.join(dataPath,'new')
param1['docTermFileName']='docTerm.utx'
param1['queryTermFileName']='queryTerm.utx'
param1['docFileName']='docs.utx'
param1['termFileName']='terms.utx'
param1['queryFileName']='queryNames.utx'
param1['queryRelevantFileName']='queryRelevants.utx'
param1['precRecallFileName']='precRecall.utx'
param1['finalScoreFileName']='finalScore_TFNONENONE_TFNONE.utx'
options={}
options['cutType']='cutNumber'
options['cutNumber']=25
options['cutMin']=0.5
options['docLocalWeight']='TF'
options['docGlobalWeight']='NONE'    #IDF NONE  BINARY Entorpy IDFB IDFP
options['docNormal']='NONE'     #COSINE NONE PUQN
options['queryLocalWeight']='TF'    #NONE BINARY
options['queryGlobalWeight']='NONE'
options['all']=False
options['withStem']=False
class lsiOptionsCls:
    autoFindCut=False
    minEigenValue=1e-12
options['lsi']=lsiOptionsCls
param1['resultPath']=os.path.join(dataPath,'weightResult')
runProgram.runProgram(param1,uniformFunction,stemFunction,mapUnicodeCp1256.mapCp1256ToUnicode,options)
options['withStem']=True
param1['resultPath']=os.path.join(dataPath,'weightStemResult')
runProgram.runProgram(param1,uniformFunction,stemFunction,mapUnicodeCp1256.mapCp1256ToUnicode,options)

print 'main.py was ended normally  ::: ahmad yousefan message   '
