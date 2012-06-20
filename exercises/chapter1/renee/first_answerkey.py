"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import survey
import thinkstats

def PartitionRecords(table): # Takes in a table and return two lists of records; firsts and non-firsts
    """Divides records into two lists: first babies and others.

    Only live births are included

    Args:
        table: pregnancy Table
    """
    firsts = survey.Pregnancies() # What data type is this? A: A python object with attirbutes that come from the list of fields
    others = survey.Pregnancies()

    for p in table.records:
        # skip non-live births
        if p.outcome != 1: # Why build a conditional in for non live births?
            continue

        if p.birthord == 1:
            firsts.AddRecord(p)
        else:
            others.AddRecord(p)

    return firsts, others


def Process(table): # Does this return anything? It does give us summary data that we can call later. Is it OK if a method doesn't return anything?
    """Runs analysis on the given table.
    
    Args:
        table: table object
    """
    table.lengths = [p.prglength for p in table.records]
    table.n = len(table.lengths)
    table.mu = thinkstats.Mean(table.lengths)


def MakeTables(data_dir='.'):
    """Reads survey data and returns tables for first babies and others."""
    table = survey.Pregnancies() # New instance of the Pregnancies class
    table.ReadRecords(data_dir)

    firsts, others = PartitionRecords(table)
    
    return table, firsts, others


def ProcessTables(*tables):
    """Processes a list of tables
    
    Args:
        tables: gathered argument tuple of Tuples
    """
    for table in tables:
        Process(table)
        
        
def Summarize(data_dir):
    """Prints summary statistics for first babies and others.
    
    Returns:
        tuple of Tables
    """
    table, firsts, others = MakeTables(data_dir) # (B) First you make tables that will create three seperate python objects, each of which is like a list of records. Table is just a new instance of the Pregnancies class that comes from our data source, first and others are sub lists of live births (first births and not first births)
    ProcessTables(firsts, others) #(C) Then you run ProcessTables to be able to get summary data on your two tables
        
    print 'Number of first babies', firsts.n #(D) Then you print what you know
    print 'Number of others', others.n

    mu1, mu2 = firsts.mu, others.mu

    print 'Mean gestation in weeks:' 
    print 'First babies', mu1 
    print 'Others', mu2
    
    print 'Difference in days', (mu1 - mu2) * 7.0 # (E) And compare it


def main(name, data_dir='.'): # (A) The main method calls Summarize first
    Summarize(data_dir)
    

if __name__ == '__main__':
    import sys
    main(*sys.argv)