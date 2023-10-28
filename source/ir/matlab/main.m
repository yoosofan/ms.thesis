%=============================================================
% Main Program for generating results - mon Sept 25, 2000
% By: Maziar Salehi
%=============================================================
DocLocalWeighting='tf';
DocGlobalWeighting='idfb';
DocNormalWeighting='cosine';
QueryLocalWeighting='tf';
QueryGlobalWeighting='idfb';
ResultMethod='DCV';

% Document Cutoff Variable (DCV)
DCV=15;  %35;
% Max Penalty for ARP
Max_Penalty=10*DCV;
% AIP point numbers
AIP_PointNums=11

TermIndexFile='didx300cran.txt'; % 'didx100cran.txt'; %  %'.\med\didx1033.txt'; %'didx100cran.txt';   %'didx45.txt';
QueryIndexFile='qidx75cran.txt'; %'qidx50cran.txt';%'.\med\qidx30.txt';  %'qidx50cran.txt';   %'tf_query.txt'; %'qindex.txt';
RelationFile='rel50cran.txt'; %'rel50300.txt';  %'.\med\qrel30.txt';    %'rel50cran.txt'; %'qrels.txt'; % %; %'rel50cran.txt'; %'qrels.txt'; %'rel4510.txt';  



%The number of documents in the collection
global N_Docs;
global N_Queries;
global N_Terms;
global LWeights;
global GWeights;
global Term_Doc_Matrix;
%global U;
%global S;
%global V;

N_Docs=300%100 %1400 %1033;
N_Queries=75%50 %225 %30;
N_Terms=30020 %20050;

% queries in CRAN subset collection that haven't any result in this subset 50 query
%No_Result=[4 5 10 15 16 17 18 23 25:36 41 42 45 47:49];
No_Result=[1:50];


%=============================================================
% Reading Document Index file 
% Term_Doc_Matrix  DF_Matrix
%=============================================================
disp('Reading Documents ............');
Temp=ReadIndex(TermIndexFile);
Term_Doc_Matrix=Temp.first;
DF_Matrix=Temp.second;
%save tdocmed1033 Term_Doc_Matrix
%save dfmed1033 DF_Matrix

%load tdocmed1033 Term_Doc_Matrix
%load dfmed1033 DF_Matrix

save tdoccran30075 Term_Doc_Matrix
save dfcran30075 DF_Matrix

%save tdoccran100 Term_Doc_Matrix
%save dfcran100 DF_Matrix
%clear Temp;
%load  tdoccran100 %tdoccran225 %tdoccran100 % % %tdoccran225  %tdoccran225
%load  dfcran100 %dfcran225 %dfcran100 %dfcran225 %dfcran100 %dfcran100 %dfcran225

%=============================================================
% Calculating Local weights
%=============================================================
pack
switch upper(DocLocalWeighting)
   
%------------ Binary Term weighting
case 'BINARY'
   disp('Calculating Binary weights')
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   Weights=ones(size(Weights,1),size(Weights,2));
   LWeights=sparse(Row,Col,Weights,N_Terms,N_Docs);
   clear Row;
   clear Col;
   clear Weights;
   
%------------ Term Frequency Weights   
case 'TF'
   disp('Local Weights by Term Frequency')
   LWeights=Term_Doc_Matrix;   
   
%------------ Calculating LSI weights   
case 'LSI'   
   disp('LSI method using truncated SVD')
   %Term_Doc_Matrix=MYUNIT(Term_Doc_Matrix);
   %[A1,k1,infoloss1,A2,k2,infoloss]=MYSVD(Term_Doc_Matrix);
   %load lsilog4510
   %Term_Doc_Matrix=A1;
   %LWeights=A1;
   %clear A1;
   
   %load lsi225cran
%--------- Calculating Singhal TF normalized weights
case 'SINGHAL' 
   disp('Calculating Singhal TF normalized weights');
   %singhal;
     
%------------- Calculating Log Weights   
case 'LOGA' 
   disp('Calculating LOGA weights');
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   LTemp=Weights;
   for i=1:size(Weights,1)
      LTemp(i,1)=1+log2(Weights(i,1));
   end
   LWeights=sparse(Row,Col,LTemp,N_Terms,N_Docs);
   clear Row;
   clear Col;
   clear Weights;
   clear LTemp;
   
%------------- Calculating LOGG Weights   
case 'LOGG' 
   disp('Calculating LOGG weights');
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   LTemp=Weights;
   for i=1:size(Weights,1)
      LTemp(i,1)=.2+(.8*log2(Weights(i,1)+1));
   end
   LWeights=sparse(Row,Col,LTemp,N_Terms,N_Docs);
   clear Row;
   clear Col;
   clear Weights;
   clear LTemp;
   
%------------- Calculating LogN Weights   
case 'LOGN'
   disp('Calculating LOGN weights');
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   LTemp=Weights;
   for i=1:size(Weights,1)
      TermNum=size(find(Col==Col(i,1)),1); % #Terms in one Col (Doc)
      Den=(1/TermNum)*(sum(Weights(find(Col==Col(i))))); % find the denominator
      LTemp(i,1)=(1+log2(Weights(i,1)))/(1+log2(Den));
   end
   LWeights=sparse(Row,Col,LTemp,N_Terms,N_Docs);

%------------- Calculating ATFA Weights   
case 'ATFA'
   disp('Calculating ATFA weights');
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   LTemp=Weights;
   for i=1:size(Weights,1)
      TermNum=size(find(Col==Col(i,1)),1); % #Terms in one Col (Doc)
      Den=(1/TermNum)*(sum(Weights(find(Col==Col(i))))); % find the denominator
      LTemp(i,1)=.9+(.1*(Weights(i,1)/Den));
   end
   LWeights=sparse(Row,Col,LTemp,N_Terms,N_Docs);

%------------- Calculating ATF1 Weights   
case 'ATF1'
   disp('Calculating ATF1 weights');
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   LTemp=Weights;
   for i=1:size(Weights,1)
      MaxTerm=max(Weights(find(Col==Col(i,1))));
      LTemp(i,1)=.5+(.5*(Weights(i,1)/MaxTerm));
   end
   LWeights=sparse(Row,Col,LTemp,N_Terms,N_Docs);
   
%------------- Calculating ATFC Weights   
case 'ATFC'
   disp('Calculating ATFC weights');
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   LTemp=Weights;
   for i=1:size(Weights,1)
      MaxTerm=max(Weights(find(Col==Col(i,1))));
      LTemp(i,1)=.2+(.8*(Weights(i,1)/MaxTerm));
   end
   LWeights=sparse(Row,Col,LTemp,N_Terms,N_Docs);
   
%------------- Calculating SQRT
case 'SQRT'
   disp('Calculating SQRT weights')
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   Weights=sqrt(Weights-.5)+1;
   LWeights=sparse(Row,Col,Weights,N_Terms,N_Docs);
   
end    % end of Local switch
%===============================================================
% Calculating Global weights
%===============================================================
   
%-------------------- Calculating IDF Matrix
disp('Building IDF matrix')
[Row,Col,V]=find(DF_Matrix);
V(1,:)=1./V(1,:);
%N_Uniqe_Terms=size(find(V==1),2);  %N_Uniqe_Terms for Singhal weighting
%pivot=N_Uniqe_Terms/N_Docs;        % pivot for Singhal weighting 
DF_Matrix=sparse(Row,Col,V,1,N_Terms);
clear Row;
clear Col;
clear i;
clear j;

switch upper(DocGlobalWeighting)

%------------- No Global weights
case 'NONE'
   disp('No Global weight')
   [Row2,Col2,V]=find(DF_Matrix);
   V=ones(size(V,1),size(V,2));
   GWeights=sparse(Row2,Col2,V,1,N_Terms);
   clear Row2;
   clear Col2;
   clear V;
%------------- Calculating Entropy weight
case 'ENTROPY' 
   disp('Calculating Entropy weights')
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   [Row2,Col2,V]=find(DF_Matrix);
   for Cnt=1:size(V,1)
      Temp=Weights(Col2(1,Cnt),1)*V(Cnt,1);
      V(Cnt,1)=(Temp*log2(Temp))/log2(N_Docs);
   end
   V=1-sum(V);
   GWeights=sparse(Row2,Col2,V);
   clear Row2;
   clear Col2;
   clear V;
   clear Temp;
   clear Cnt;
   
%------------- Calculating IDFB weight
case 'IDFB'
   disp('Calculating IDFB weights')
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   [Row2,Col2,V]=find(DF_Matrix);
   for Cnt=1:size(V,2)
      Den=size(find(Term_Doc_Matrix(Col2(Cnt),:)),2);
      V(1,Cnt)=log2(N_Docs/Den);
   end
   GWeights=sparse(Row2,Col2,V);
   clear Row;
   clear Col;
   clear Weights;
   clear Row2;
   clear Col2;
   clear V;

%------------- Calculating IDFP weight
case 'IDFP'
   disp('Calculating IDFP weights')
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   [Row2,Col2,V]=find(DF_Matrix);
   for Cnt=1:size(V,2)
      Den=size(find(Term_Doc_Matrix(Col2(Cnt),:)),2);
      V(1,Cnt)=log2((N_Docs-Den)/Den);
   end
   GWeights=sparse(Row2,Col2,V);
   clear Row;
   clear Col;
   clear Weights;
   clear Row2;
   clear Col2;
   clear V;
   
%------------- Calculating IGFF weight
case 'IGFF'
   [Row2,Col2,V]=find(DF_Matrix);
   for Cnt=1:size(V,2)
      Den=size(find(Term_Doc_Matrix(Col2(Cnt),:)),2);
      V(1,Cnt)=(1/(V(1,Cnt)*Den));
   end
   GWeights=sparse(Row2,Col2,V);
   clear Row2;
   clear Col2;
   clear V;
   
%------------- Calculating IGFL weight
case 'IGFL'
   [Row2,Col2,V]=find(DF_Matrix);
   for Cnt=1:size(V,2)
      Den=size(find(Term_Doc_Matrix(Col2(Cnt),:)),2);
      V(1,Cnt)=log2(   (   1/(V(1,Cnt)*Den)   )+1   );
   end
   GWeights=sparse(Row2,Col2,V);
   clear Row2;
   clear Col2;
   clear V;
   
%------------- Calculating IGFI weight
case 'IGFI'
   [Row2,Col2,V]=find(DF_Matrix);
   for Cnt=1:size(V,2)
      Den=size(find(Term_Doc_Matrix(Col2(Cnt),:)),2);
      V(1,Cnt)=(1/(V(1,Cnt)*Den))+1;
   end
   GWeights=sparse(Row2,Col2,V);
   clear Row2;
   clear Col2;
   clear V;
   
%------------- Calculating IGFS weight
case 'IGFS'
   [Row2,Col2,V]=find(DF_Matrix);
   for Cnt=1:size(V,2)
      Den=size(find(Term_Doc_Matrix(Col2(Cnt),:)),2);
      V(1,Cnt)=sqrt((1/(V(1,Cnt)*Den))-.9);
   end
   GWeights=sparse(Row2,Col2,V);
   clear Row2;
   clear Col2;
   clear V;

end   % end of Global Weight

%===============================================================
% Calculating Normalized weights
%===============================================================

switch upper(DocNormalWeighting)
   
%------------ Pivoted Unique Normalization   
case 'PUQN'
   disp('Calculating Pivoted Unique Normalization Weights');
   slope=.2;
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   TempWeights=Weights;
   N_Uniqe_Terms=zeros(1,N_Docs);
   for i=1:N_Docs
      ColMem=find(Col==i);
      for j=1:max(size(ColMem))
         if Weights(ColMem(j))==1 
            N_Uniqe_Terms(i)=N_Uniqe_Terms(i)+1;
         end
      end
   end
   pivot= sum(N_Uniqe_Terms)/N_Docs;   
   
   for i=1:size(Weights,1)
      TempWeights(i)=1/ ( ((1-slope)*pivot) + (slope * N_Uniqe_Terms(Col(i))) );
   end
   
   NWeights=sparse(Row,Col,TempWeights,N_Terms,N_Docs);
   clear Row;
   clear Col;
   clear TempWeights;
   
   
%------------ Cosine Normalization   
case 'COSINE'
   disp('Calculating COSINE normalized weights')
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   
   %TempWeights=Weights;
   %for i = 1:size(Weights,2)
   %   TempWeights(:,i) = 1 ./ (norm( Weights(:,i),2 ));
   %end
   
   [M,N]=size(Weights);
   TempWeights=ones(M,N);
   NWeights=sparse(Row,Col,TempWeights,N_Terms,N_Docs);
   clear TempWeights;
   clear Row;
   clear Col;

end % Switch Document normalization
%===============================================================
% Calculating final document weights
%===============================================================
disp('Calculating final Document weights')
switch upper(DocLocalWeighting)
case 'LSI'
   
otherwise
[Row,Col,Weights]=find(LWeights);
[Row2,Col2,Weights2]=find(NWeights);
for i=1:size(Weights,1)
  Weights(i,1)=Weights(i,1)*GWeights(1,Row(i))*Weights2(i,1);
end
Final_Weights=sparse(Row,Col,Weights,N_Terms,N_Docs);
clear Row;
clear Col;
clear i;
clear Weights;
clear Weights2;
clear Col2;
clear Row2;
%save  FDOCmed30ltc2  Final_Weights
%save FDOCcran225ltc2  Final_Weights % for genetic optimization 
%save FDOCcran50ltc2  Final_Weights % for genetic optimization 
%save FDOCcran50tfidf  Final_Weights % for genetic optimization 
save FDOCcran75300tfidf  Final_Weights % for genetic optimization 

end
%-------------------------------------------------------------------
%---------------------------------- Query processing ---------------
%-------------------------------------------------------------------
disp('processing query')

%=========================================================
% Reading Query indices
%=========================================================
disp('Reading Queries ............');
Query_Matrix=ReadQury(QueryIndexFile);
%save Q30med Query_Matrix
%load  Q30med

%save Q50cran Query_Matrix
%load  q50cran %Q225Matrix %q50cran  %
save Q75cran Query_Matrix

%=========================================================
%Calculating Query Local Weights
%=========================================================
switch upper(QueryLocalWeighting)

%------------ Binary Term weighting
case 'BINARY'
   disp('Calculating Binary weights')
   [Row,Col,Weights]=find(Query_Matrix);
   Weights=ones(size(Weights,1),size(Weights,2));
   LQWeights=sparse(Row,Col,Weights,N_Terms,N_Queries);
   clear Row;
   clear Col;
   clear Weights;

%----------------- Query Term frequency weighting
case 'TF'
   disp('Query Term frequency weighting')
   LQWeights=Query_Matrix;

%----------------- Calculating Log Weights
case 'LOGA' 
   disp('Calculating Query LOG weights');
   [Row,Col,Weights]=find(Query_Matrix);
   LTemp=Weights;
   for i=1:size(Weights,1)
      LTemp(i,1)=log2(Weights(i,1)+1);
   end
   LQWeights=sparse(Row,Col,LTemp,N_Terms,N_Queries);
   clear Row;
   clear Col;
   clear Weights;
   clear LTemp;
   
%------------- Calculating LOGG Weights   
case 'LOGG' 
   disp('Calculating LOGG weights');
   [Row,Col,Weights]=find(Query_Matrix);
   LTemp=Weights;
   for i=1:size(Weights,1)
      LTemp(i,1)=.2+(.8*log2(Weights(i,1)+1));
   end
   LQWeights=sparse(Row,Col,LTemp,N_Terms,N_Queries);
   clear Row;
   clear Col;
   clear Weights;
   clear LTemp;
   
%-------- Calculating Query SMART Buckley weights
case 'BUCK' 
   disp('calculating Query SMART Buckley weights');
   Max=max(full(Query_Matrix),[],1);
   [Row,Col,Weights]=find(Query_Matrix);
   for i=1:size(Weights,1)
      Weights(i,1)=(.5+(.5*Weights(i,1)/Max(Col(i))));
   end
   LQWeights=sparse(Row,Col,Weights,N_Terms,N_Queries);
   clear Row;
   clear Col;
   clear i;
   clear Weights;
   clear Max;
   
%------------- Calculating ATF1 Weights   
case 'ATF1'
   disp('Calculating ATF1 weights');
   [Row,Col,Weights]=find(Query_Matrix);
   LTemp=Weights;
   for i=1:size(Weights,1)
      MaxTerm=max(Weights(find(Col==Col(i,1))));
      LTemp(i,1)=.5+(.5*(Weights(i,1)/MaxTerm));
   end
   LQWeights=sparse(Row,Col,LTemp,N_Terms,N_Queries);
   clear Row;
   clear Col;
   clear i;
   clear Weights;
   clear Max;
   
   
end  %end of local query switch 
%=========================================================
% Calculating Query Global Weights
%=========================================================
switch upper(QueryGlobalWeighting)
   
%------------- No Global weights
case 'NONE'
   disp('No Global weight')
   [Row2,Col2,V]=find(DF_Matrix);
   V=ones(size(V,1),size(V,2));
   GQWeights=sparse(Row2,Col2,V,1,N_Terms);
   clear Row2;
   clear Col2;
   clear V;
   
%------------- Entropy weight   
case 'ENTROPY' 
   disp('Calculating Entropy weights')
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   [Row2,Col2,V]=find(DF_Matrix);
   for Cnt=1:size(V,1)
      Temp=Weights(Col2(1,Cnt),1)*V(Cnt,1);
      V(Cnt,1)=(Temp*log2(Temp))/log2(N_Docs);
   end
   V=1-sum(V);
   GQWeights=sparse(Row2,Col2,V);
   clear Row2;
   clear Col2;
   clear V;
   clear Temp;
   clear Cnt;
   
%------------- Calculating IDFB weight
case 'IDFB'
   disp('Calculating IDFB weights')
   [Row,Col,Weights]=find(Term_Doc_Matrix);
   [Row2,Col2,V]=find(DF_Matrix);
   for Cnt=1:size(V,2)
      Den=size(find(Term_Doc_Matrix(Col2(Cnt),:)),2);
      V(1,Cnt)=log2(N_Docs/Den);
   end
   GQWeights=sparse(Row2,Col2,V);
   clear Row;
   clear Col;
   clear Weights;
   clear Row2;
   clear Col2;
   clear V;
   
   
end; % switch query global weighting

%=========================================================
% Calculating Final Query Weights
%=========================================================
disp('Calculating final Query weights')

[Row,Col,Weights]=find(LQWeights);
for i=1:size(Weights,1)
  Weights(i,1)=Weights(i,1)*GQWeights(1,Row(i));
end

Final_Query_Weights=sparse(Row,Col,Weights,N_Terms,N_Queries);
clear Row;
clear Col;
clear i;
clear Weights;
clear Query_Matrix;

%save FQcran225 Final_Query_Weights %for genetic optimization
%save FQcran50 Final_Query_Weights %for genetic optimization
%save FQcran50tfidf Final_Query_Weights %for genetic optimization
%save FQcran50ltc2 Final_Query_Weights %for genetic optimization

save FQcran75300tfidf Final_Query_Weights %for genetic optimization
%--------------------------------------------------------------------
%---------------------------- Retrieval Process ---------------------
%--------------------------------------------------------------------
disp('Retrieval process')

%=======================================================
% Calculating Similarity
%=======================================================
pack 
disp('Calculating silmilarity')
switch upper(DocLocalWeighting)
case 'LSI'
  %Sim_Matrix=LSIsim(Final_Query_Weights);
  %load lsi225cran
  load lsi30medltc2
  
  P=S*V';
  C=U'*Final_Query_Weights;
  
  NormDoc=zeros(1,N_Docs);  % Norm of each Doc
  
  for i=1:N_Docs
     NormDoc(i)= norm(P(:,i));
  end
  NormQue=zeros(1,N_Queries);  % Norm of each Query
  for i=1:N_Queries
     %NormQue(i)= norm(C(:,i));
     NormQue(i)=norm(Final_Query_Weights(:,i));
  end
  for i=1:N_Queries
     for j=1:N_Docs
        Sim_Matrix(i,j)=(P(:,j)'*C(:,i))/(NormDoc(j)*NormQue(i));
     end
  end
  

%-----------------------------------------------  
otherwise
switch upper(DocNormalWeighting)
   
%--------------- Cosine Similarity   
case 'COSINE'   
   %load 
   for i=1:N_Queries 
      %if isempty(find(No_Result==i)) 
         Sim_Matrix(i,:)=MYCOS(Final_Weights,Final_Query_Weights(:,i));
         if (i/10==fix(i/10)) 
            i
            pause(160); 
         end; 
      %else
      %   Sim_Matrix(i,:)=zeros(1,N_Docs);
      %end;
   end
   clear i;
   
%-------------- Singhal Similarity   
case 'PUQN'
   for i=1:N_Queries 
      %if isempty(find(No_Result==i))
         Sim_Matrix(i,:)=MYSIM(Final_Weights,Final_Query_Weights(:,i));
         if (i/10==fix(i/10)) 
            i
            pause(160); 
         end; 
      %else
      %   Sim_Matrix(i,:)=zeros(1,N_Docs);
      %end;

   end
   clear i;

end;   % switch similarity

%save sim30medlog Sim_Matrix
%save sim50cranTF Sim_Matrix
%stem(1:45,Sim_Matrix(1,:));
%pause;
end    % LSI switch
%=======================================================
% Seperate the results
%=======================================================
switch upper(ResultMethod)
   
%----------- Threshold Method   
case 'THR'   
   % Cutoff Threshold 
   Threshold=.1
   
   % getting results
   disp('getting results by Threshold method')
   for i=1:size(Sim_Matrix,1) 
      Results(i,:)={find(Sim_Matrix(i,:)>Threshold)};
   end
   
%----------- DCV Method   
case 'DCV'
   
   
   % getting results
   disp('getting results by DCV Method')
   for i=1:size(Sim_Matrix,1) 
      Results(i,:)={findNmax(Sim_Matrix(i,:),DCV)};
   end
   
end  % ResultMethod switch
%========================================================
% Evaluate the results
%========================================================

%Reading relation matrix
%Rel_Matrix = ReadRel(RelationFile);
%save rel30med Rel_Matrix
%load rel30med

%save rel50300cran Rel_Matrix
%save rel50cran Rel_Matrix
%load rel225mat
load rel50cran

%---------------------------- Calculating correct answers of system
Correct=zeros(1,N_Queries);

for i=1:size(Results,1)
   for j=1:size(Results{i},2)
      if Rel_Matrix(i,Results{i}(j))==1 
         Correct(i)=Correct(i)+1;
      end   
   end
end


%---------------------------- Calculating Recall and Precision 
disp('Calculating Recall and Precision')

for i=1:N_Queries
   if sum(Rel_Matrix(i,:)) ~= 0
      Recall(i)=100*Correct(i)/sum(Rel_Matrix(i,:));
   else
      Recall(i)=0;
   end
   if size(Results{i},2)~=0
      Precision(i)=100*Correct(i)/size(Results{i},2);
   else
      Precision(i)=0;
   end
end

%clear Correct;
clear i;
%clear Results;
%Precision 
%Recall
%pause

% ------------------- Calculating Non-Interpolated Average precision

for i=1:N_Queries
   Act_Results=find(Rel_Matrix(i,:)==1);
   [Val,Idx]=sort(Sim_Matrix(i,:));
   
   % find the results position
   for j=1:length(Act_Results)
      TempRes_Position(j)=find(Idx==Act_Results(j));
   end
   TempRes_Position=sort(N_Docs+1-TempRes_Position);
   
   % find the Detail precision for any query
   for j=1:length(TempRes_Position)
      TempDetail_Pr(j)=j/TempRes_Position(j);
   end
   
   % store Result positions and detail presicion in cells
   Res_Positions{i}=TempRes_Position;
   Detail_Pr{i}=TempDetail_Pr;
   
   
   % find non interpolated average precision for this query
   if (length(TempDetail_Pr)==0)
      All_NAP(i)=0;
      else
         All_NAP(i)=mean(TempDetail_Pr);
      end
   TempRes_Position=[];
   TempDetail_Pr=[];
end

NAP=mean(All_NAP(find(All_NAP)));
clear i;
clear j;

% ------------------- Calculating Interpolated Average precision

for i=1:N_Queries
   TempRes_Position=Res_Positions{i}(:);
   TempRes_Position=TempRes_Position';
   TempDetail_Pr=Detail_Pr{i}(:);
   TempDetail_Pr=TempDetail_Pr';
   
   if length(TempDetail_Pr)==0
      PPrecision=[];
   else
      for j=1:AIP_PointNums
         if ceil(  length(TempDetail_Pr)*((j-1)/(AIP_PointNums-1)))==0
            PPrecision(j)= ...
               max(TempDetail_Pr(1:length(TempDetail_Pr)));
         else
            PPrecision(j)= ...
               max(TempDetail_Pr(ceil(  length(TempDetail_Pr)*((j-1)/(AIP_PointNums-1))) :length(TempDetail_Pr)));
         end
      end
   end   
   
   if (length(PPrecision)==0)
      All_IAP(i)=0;
   else
      All_IAP(i)=mean(PPrecision);
   end;
   
   
   if isempty(PPrecision)
      All_PPr(i,:)=zeros(1,11);
   else
      All_PPr(i,:)=PPrecision;
   end
   
   PPrecision=[];
end
IAP=mean(All_IAP(find(All_IAP)));

%save PRcranlog All_PPr
%hold on
%grid on
%plot(0:.1:1, mean(All_PPr,1),'g:');

%------------------- Calculating Average Ranked precision
%Ranked_Results=readrankrel(RelationFile);
%save rrel30med  Ranked_Results
%load rrel30med

%save rrel50300cran  Ranked_Results
%save rrel225cran  Ranked_Results
%load rrel225cran
load rrel50cran

for i=1:N_Queries
%find the difference between actual and ideal result positions in DCV range
% if result is not in the range add the Max penalty value

   TempRanked_Results=Ranked_Results{i}(:);
	TempRanked_Results=TempRanked_Results';

   [Val,Idx]=sort(Sim_Matrix(i,:));
   
   % find the results position
   for j=1:length(TempRanked_Results)
      TempRes_Position(j)=find(Idx==TempRanked_Results(j));
   end
   
   if length(TempRes_Position)==0
      All_ARP(i)=0;
   else
      TempRes_Position=N_Docs+1-TempRes_Position;
      dif=0;
      DC_dif=0;
      RelNum=0;
      for j=1:length(TempRes_Position)
         if (TempRes_Position(j) > DCV)
            dif=dif+abs(j-TempRes_Position(j))+(abs(DCV-TempRes_Position(j)));
            DC_dif=DC_dif+Max_Penalty;
         else
            dif=dif+abs(j-TempRes_Position(j));
            DC_dif=DC_dif+abs(j-TempRes_Position(j));
            RelNum=RelNum+1;
         end
      end
      Res_Len=length(TempRanked_Results);
      Den2=( (Res_Len*(N_Docs-DCV))-((Res_Len+1)*(Res_Len+2)/2));
      Den1=(Res_Len*N_Docs)-(Res_Len^2);
      All_ARP(i)=1-(dif/(Den2+Den1));                %Average ranked precision  
      DC_All_ARP(i)=1-(DC_dif/(Res_Len*Max_Penalty));   %Document cutoff ARP
      TempRes_Position=[];
   end
   
end

ARP=mean(All_ARP(find(All_ARP)));
DC_ARP=mean(DC_All_ARP(find(DC_All_ARP)));

%===========================================================
% save the results
%===========================================================
save PR30medLsiltc2 All_PPr Precision Recall DC_ARP ARP NAP IAP

EvalFile=fopen('Evalmed.txt','at+');

%(Doc weighting function) N_Docs (Query weighting function) N_Queries (Threshold or DCV)...
% Threshold or DCV value
if ResultMethod=='THR'
fprintf(EvalFile,'%s %s %s %d %s %s %d %s %4.2f\n',DocLocalWeighting,DocGlobalWeighting...
        ,DocNormalWeighting,N_Docs,QueryGlobalWeighting,QueryLocalWeighting,...
        N_Queries,ResultMethod,Threshold);
  else
     fprintf(EvalFile,'%s %s %s %d %s %s %d %s %d\n',DocLocalWeighting,DocGlobalWeighting...
        ,DocNormalWeighting,N_Docs,QueryGlobalWeighting,QueryLocalWeighting,...
        N_Queries,ResultMethod,DCV);
  end

%---------------------------------------- writing Recall
NonZ=find(Recall);
fprintf(EvalFile,'%5d',NonZ);
fprintf(EvalFile,'\n');
fprintf(EvalFile,'%8.4f ',Recall(NonZ));
fprintf(EvalFile,'\n');

%----------------------------------------- writing Precision
NonZ=find(Precision);
fprintf(EvalFile,'%5d',NonZ);

fprintf(EvalFile,'\n');
fprintf(EvalFile,'%8.4f ',Precision(NonZ));
fprintf(EvalFile,'\n');

fclose(EvalFile);
%===========================================================
% Plot the results 
%===========================================================
YPlot=zeros(1,AIP_PointNums);
for i=1:AIP_PointNums
   YPlot(i)=mean( All_PPr(find(All_PPr(:,i)),i) );
end
plot(0:.1:1,YPlot,'r');

%===========================================================
% sending data to Excel 
% All_PPr Precision Recall DC_ARP ARP NAP IAP
%===========================================================
disp('Sending data to Excel')

% Initialize conversation with Excel.
chan = ddeinit('excel', 'Sheet1');

%data=[Recall(NonZ)];

% Set range of cells in Excel for poking.
%range = 'r3c1:r3c10';
% Poke the z data to the Excel spread sheet.
%rc = ddepoke(chan, range, data);

%data=[Precision(NonZ)];

% Set range of cells in Excel for poking.
%range = 'r4c1:r4c10';
% Poke the z data to the Excel spread sheet.
%rc = ddepoke(chan, range, data);

data=[mean(Recall(NonZ))];
range='r3c2';
rc = ddepoke(chan, range, data);

data=[mean(Precision(NonZ))];
range='r3c1';
rc = ddepoke(chan, range, data);

data=[NAP];
range='r3c5';
rc = ddepoke(chan, range, data);

data=[IAP];
range='r3c6';
rc = ddepoke(chan, range, data);

data=[ARP];
range='r3c4';
rc = ddepoke(chan, range, data);

data=[DC_ARP];
range='r3c3';
rc = ddepoke(chan, range, data);

data=[YPlot];
range='r5c2:r5c13';
rc = ddepoke(chan, range, data);

% Terminate the DDE conversation with excel
ddeterm(chan);

