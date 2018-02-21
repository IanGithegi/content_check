# List All files within a folder. To much a certain criteria
import os
path = 'test_folder'
bdfiles = open(path+"/bdfiles.txt", "w")
print path


def content_count(path):
    print("----------Show Files and count on Each directory")
    print 'Number of Folders is %d' % len(os.listdir(path))

    for root, dir, filenames in os.walk(path):
        count = 0
        dir = [d for d in dir if not d[0] == '.']
        filenames = [f for f in filenames if not f[0] == '.']
        print ('Directory: is %s' % root)
        for f in filenames:
                print('\t%s' % f)
                count += 1
        if (count > 4):
            print 'Check bdfiles.txt for Results'
            print >> bdfiles, '%d Extra File(s) in %s. Remove Files' % (count - 4, root)
        else:
            print (count == 4)


content_count(path)
