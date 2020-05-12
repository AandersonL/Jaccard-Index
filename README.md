# Jaccard Index

[Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index) is a formula to determine the similarity between two sets.

![](formula.svg)

We get the intersection between two sets and divide by his union, this will give a number between 0-1, the good score for your problem is up to you to.


### Simple example

```python
>>> import jaccard
>>> setA = ["House", "Something", 3, "MyFunction"]
>>> setB = ["Country", 0.3, "Something"]
>>> jaccard.jaccard_index(setA,setB)
0.16666666666666666
```

### PE file import table similarity
```python
>>> sample1IAT
['HeapSize', 'GetLastError', 'InitializeCriticalSectionAndSpinCount', 'HeapFree', 'GetStdHandle', 'EnterCriticalSection', 'LCMapStringW', 'OutputDebugStringW', ...]
>>> sample2IAT
['HeapFree', 'FreeLibrary', 'ExitProcess', 'RtlUnwind', 'SizeofResource', 'GetCurrentDirectoryA', 'LocalAlloc', 'LockResource', 'GetWindowsDirectoryA', ...]
>>> jaccard.jaccard_index(sample1IAT, sample2IAT)
0.2077922077922078
```

There is a lot of usage for this simple function.

## Just one function ?

Yep, i did'nt find any Python script to this simple function, so a decided to create that.


Thanks
