function answer = prc_recal_func(term_doc,term_query,query_doc,Tr,no)
%from behdad
%clear
%load cran_svd_100
time = cputime;
t = size(term_doc);
doc_no = t(2);
%zeros = 0;
%Tr = .2;  %thereshhold
for (i = 1:11)
   PlotArr(i) = 0;
end
count = 0;
for i = 1:no
   disp(i)
   count = count + 1;
   x = term_query(:,i);
   x = x';
   for j = 1:doc_no
      y = term_doc(:,j);
      y = y';
      sim(j) = (x*y') / sqrt((x*x') * (y * y'));
   end
   a = find(sim > Tr);
   b = sim(a);
   ss = size(b);
   ranked = b;
   if ss(1) ~= 0
     z = fix(b(1,:)*100)*10000;
     z = -(z(1,:) + a);
     z = -sort(z);
     ranked = mod(z, 10000);
   end  
   relev = find(query_doc(i, :));
   t = size(relev);
   A_No = t(2);
   t = size(ranked);
   B_No = t(2);
   %   Max = max(A_No, B_No);
   clear Recal;
   clear Prec;
   for (j = 1:B_No)
      t = size(intersect(relev,ranked(1:j)));
      AIntersectB = t(2);
      Recal(j) = AIntersectB / A_No;
      Prec(j) = AIntersectB / j;
   end
   Recal(B_No + 1) = 0;
   Prec(B_No + 1) = 0;

   ind = 1;
   pind = 1;
   for (k = 0:0.1:1)
      while (ind < B_No + 1 & Recal(ind) < k)
         ind = ind + 1;
      end
      PlotArr2(pind) = max(Prec(ind:B_No+1));
      PlotArr(pind) = PlotArr(pind) + max(Prec(ind:B_No + 1));

      pind = pind + 1;
   end   
   if B_No == 0
     zeros = zeros + 1;
  end   
%  PlotArr(1)/count
%  plot(0:.1:1, PlotArr2);
%  keyboard;
end
PlotArr = PlotArr / (count);
plot(0:.1:1, PlotArr);
time = (cputime - time) / 60
%zeros
count;
answer = PlotArr(1);

   
   
