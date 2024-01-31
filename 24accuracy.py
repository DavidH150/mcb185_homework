def accuracy(tp, fp, tn, fn):
	precision = tp/(tp+fp) 
	recall = tp/(tp+fn) 
	f1 = 2*(precision * recall)/(recall + precision)
	acc = (tp + tn)/(tp + fp + tn +fn)
	return f1, acc 
    

print('F1 and Accuracy', accuracy(50, 10, 100, 5))
print('F1 and Accuracy', accuracy(49, 50, 31, 3000))
