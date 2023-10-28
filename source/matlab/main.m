termDoc1=load('docTerm.txt');
[noTerm,noDoc]=size(termDoc);
termDoc=sparse(termDoc1);
clear termDoc1
pack
documentLocalWeightMethode='tf';
documnetGlobalWeightMethode='idfb';
documnetNormalWeightMethode='cosine';
queryLocalWeightMethode='tf';
queryGlobalWeightMethode='idfb';
distanceMethode='DCV';

localWeight=termDoc;
[row1,col1,w1]=find(termDoc);
noWeight=length(termDoc)
for m1=1:noWeight:
    globalWeight(m1)=log2(noDocs/size(find(termDoc(m1,:))));
for m1=:numberOfDucuments:
    normalWeight(m1)=1./(sqrt(sum((globalWeight(m1) .* localWeight(m1,:)).^2)))
finalW=