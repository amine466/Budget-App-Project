# **Arithmetic Formatter Project**  

FreeCodeCamp - **Scientific Computing with Python** (First Project)  

## 📌 **Project Overview**  
Students in primary school often arrange arithmetic problems vertically to make them easier to solve.  

For example, `"235 + 52"` becomes: 
```sh
  235
+  52
-----
```

Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example
Function Call:
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```
Output:
```sh
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```
Function Call:
```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```
Output:
```sh
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```
## ⚠️ Rules & Error Handling  
The function returns an **error message** if the input does not meet the requirements:  

- ❌ **Too many problems**: More than **5** problems → `'Error: Too many problems.'`  
- ❌ **Invalid operators**: Only **+** and **-** are allowed → `'Error: Operator must be "+" or "-".'`  
- ❌ **Non-numeric values**: Only **digits** are allowed → `'Error: Numbers must only contain digits.'`  
- ❌ **Number too large**: Each number must be **4 digits max** → `'Error: Numbers cannot be more than four digits.'` 
