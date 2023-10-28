import os,string
import prepareDocs,prepareQueries
import weight,findBest,retrievalEvaluation
import lsi
def findBestAndRetEval(options,retEvalParams):
    findBestObject=findBest.findBestCls(options['cutType'],options['cutNumber'],options['cutMin'])
    noResult=findBestObject.similarity(retEvalParams['docTermWeight'],retEvalParams['queryTerm'],retEvalParams['noQuery'],retEvalParams['noDoc'],retEvalParams['finalScoreFileName'])
    retEval=retrievalEvaluation.retrievalEvaluationCls(retEvalParams['queryRelevantFileName'],retEvalParams['docFileName'])
    retEval.run(findBestObject.finalResultArray,retEvalParams['precRecallFileName'],noResult)
def runProgram(param1,uniformFunction,stemFunction,uni2cp1256,options):
    docQueryPath=param1['docQueryPath']
    docTermFileName=os.path.join(param1['resultPath'],param1['docTermFileName'])
    queryTermFileName=os.path.join(param1['resultPath'],param1['queryTermFileName'])
    docFileName=os.path.join(param1['resultPath'],param1['docFileName'])
    termFileName=os.path.join(param1['resultPath'],param1['termFileName'])
    queryFileName=os.path.join(param1['resultPath'],param1['queryFileName'])
    retEvalParams={}
    retEvalParams['queryRelevantFileName']=os.path.join(param1['resultPath'],param1['queryRelevantFileName'])
    retEvalParams['precRecallFileName']=os.path.join(param1['resultPath'],param1['precRecallFileName'])
    retEvalParams['finalScoreFileName']=os.path.join(param1['resultPath'],param1['finalScoreFileName'])
    retEvalParams['docFileName']=docFileName
    if options['all']:
        prepDocObject2=prepareDocs.prepareDocs(docQueryPath,uni2cp1256,stemFunction)
        docsFileNames={}
        docsFileNames['docTermFileName']=docTermFileName
        docsFileNames['docsFileName']=docFileName
        docsFileNames['termsFileName']=termFileName
        prepDocObject2.run(docsFileNames,options['withStem'])
        queryObject=prepareQueries.prepareQueryCls(docQueryPath,uniformFunction,stemFunction,prepDocObject2.allTerms)
        queryObject.run(queryTermFileName,queryFileName,queryRelevantFileName,options['withStem'])
    #
    weightObject=weight.weightCls(docTermFileName,queryTermFileName,options)
    weightObject.run()
    #
    retEvalParams['docTermWeight']=weightObject.docTermWeight
    retEvalParams['queryTerm']=weightObject.queryTerm
    retEvalParams['noQuery']=weightObject.noQuery
    retEvalParams['noDoc']=weightObject.noDoc
    findBestAndRetEval(options,retEvalParams)
    # with lsi
    lsiObject1=lsi.lsiCls(retEvalParams,options['lsi'].autoFindCut,options['lsi'].minEigenValue)
    lsiObject1.run()
    retEvalParams['docTermWeight']=lsiObject1.docTermLsi
    retEvalParams['queryTerm']=lsiObject1.queryTermLsi
    print 'docTermLsi',lsiObject1.docTermLsi.getshape()
    print 'queryTerm',lsiObject1.queryTermLsi.getshape()
    l1=param1['precRecallFileName'].split('.')
    s1='lsi_'+l1[0]+'.'+l1[1]
    retEvalParams['precRecallFileName']=os.path.join(param1['resultPath'],s1)
    findBestAndRetEval(options,retEvalParams)    
    #assign new values of lsiDocTerm lsiQueryTerm
