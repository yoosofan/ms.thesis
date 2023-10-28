% from salehi 
function sims=LSIsim(q);

global N_Queries;
global N_Docs;
global U;
global S;
global V;


P=S*V';
C=U'*q;

NormDoc=zeros(1,N_Docs);  % Norm of each Doc

for i=1:N_Docs
   NormDoc(i)= norm(P(:,i));
end

NormQue=zeros(1,N_Queries);  % Norm of each Query

for i=1:N_Queries
   NormQue(i)= norm(C(:,i));
end

for i=1:N_Queries
   for j=1:N_Docs
      sims(i,j)=(P(:,j)*C(:,i))/(NormDoc(j)*NormQue(i));
   end
end

