import cv2
import os

def dataset():
    #img = cv2.imread('a.png')
    use = []
    test_labels, train_labels, test_images, train_images = [], [], [], []
    
    for _,_,files in os.walk('-0.28/and'):
        #print(files)
        for f in files:
        	if f.find('png') != -1 and f.find('and') != -1:
        		#print(f)
        		s = '-0.28/and/'+f
        		use.append(s)
        		test_labels.append('and')
        		train_labels.append('and')
        		
    for _,_,files in os.walk('-0.28/or'):
        #print(files)
        for f in files:
        	if f.find('png') != -1 and f.find('or') != -1:
        		s = '-0.28/or/'+f
        		use.append(s)
        		test_labels.append('or')
        		test_labels.append('or')
        		
    for _,_,files in os.walk('-0.28/xor'):
        #print(files)
        for f in files:
        	if f.find('png') != -1 and f.find('xor') != -1:
        		s = '-0.28/xor/'+f
        		use.append(s)
        		test_labels.append('xor')
        		test_labels.append('xor')
    
    for u in use:
    	img = cv2.imread(u)
    	print(u)
    	test_images.append(img)
    	train_images.append(img)
    	#break
    	#print(img)
    #print(test_images)     
    
    return train_images, train_labels, test_images, test_labels
    
dataset()
