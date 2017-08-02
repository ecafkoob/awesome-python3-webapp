import numpy as np
from os import sys, path
import pandas as pd
import urllib2
import json
import sys
import socket


def getData(url):
	try:
		data = json.load(urllib2.urlopen(url, timeout=1))
		return data;
	except socket.timeout as e:
		print type(e)    #catched
		return getData(url);

if __name__=='__main__':
    gene_info_file = sys.argv[1];
    output_file = sys.argv[2];
    start = int(sys.argv[3]);
    geneLen = int(sys.argv[4]);

    #open(output_file, 'w').close()   
    res= np.loadtxt("jk.csv",dtype=int)
    outputStrings = [];
    for i in range(start,start+geneLen):
        print (i+1),'/',len(res)
        gids=res[i]
        url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=' + repr(gids) + '&retmode=json';
        print url
        
        data = getData(url);
        geneId = str(gids)
        zongjie = data['result'][str(gids)]['summary']    
        if zongjie == '':
        	continue;  
        description = data['result'][str(gids)]['description']
        maplocation=data['result'][str(gids)]['maplocation']
        name = data['result'][str(gids)]['name']
        outputStrings.append(name + '||||' + geneId +'||||'+ description + '||||' + maplocation + '||||' + zongjie);
        #array=[geneId,description,maplocation,zongjie]
        #resultArray=np.array([['id','des','map','summary']])
        #currentArray=np.array([array])
        #resultArray=np.append(resultArray,currentArray,axis=0)
        #pd.DataFrame(currentArray).to_csv(output_file, index=False, mode='a', sep='^', header= (i==0))
        #print(currentArray)
        #print("%s||||%s|||||%s|||||%s"%(geneId,description,maplocation,zongjie) )

    np.savetxt(output_file, outputStrings, fmt='%s');
        
        #np.savetxt('aaa.txt',data,fmt="%s")
        #result.append([data['result'][str(i)]['summary']])
        #np.savetxt('demo.csv', result, delimiter='||||',fmt="%s")
        # result = [0]
        #for g in len(res):
        # result.append([g, data['result'][str(g)]['summary'] if str(g) in data['result'] else '']);
        #pd.DataFrame(result, columns=['gene_id', 'summary']).to_csv(output_file, index=False, mode='w', header= (i==0))

        # np.savetxt('output.csv', Output, delimiter='||||');
         