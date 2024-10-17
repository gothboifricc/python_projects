import pandas

#method1#
df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns = ["Price", "Age", "Values"], index = ["First", "Second"])
print(df1)

#method2#
df2 = pandas.DataFrame([{"Name":"John", "Surname":"Wick"}, {"Name":"Eric", "Surname":"Cartman"}], index = ["First", "Second"])
print(df2)