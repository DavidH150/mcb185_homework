def accuracy(tp, fp, tn, fn):
    precision = tp/(tp+fp) 
    recall = tp/(tp+fn) 
    f1 = 2*(precision * recall)/(recall + precision)
    acc = (tp + tn)/(tp + fp + tn +fn)
    print('F1 score:', f1)
    print('Accuracy', acc)

accuracy(50,10,100,5)
accuracy(49,50, 31, 3000)
