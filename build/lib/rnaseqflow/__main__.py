'''
Created on Dec 13, 2015

@author: justinpalpant
'''
import workflow
import neurolab

if __name__ == '__main__':
    print 'Please select the module to run:'
    print '1. Workflow'
    print '0: Quit'
    
    key = int(input('Make a selection: '))
    
    if key == 1:
        print 'Starting a preprocessing workflow...'
        workflow.main()
    