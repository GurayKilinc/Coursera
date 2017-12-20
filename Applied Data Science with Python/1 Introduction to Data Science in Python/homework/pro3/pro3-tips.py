# test output type (different, p, better)

res = run_ttest()
print('Type test:', 'Passed' if type(
    res) == tuple else 'Failed')
print('test `better` item type:','Passed' if type(res[0]) == bool or type(res[0]) == np.bool_ else 'Failed' )
print('`p` item type test:', 'Passed' if type(
    res[1]) == np.float64 else 'Failed')
print('`different` item type test:',
      'Passed' if type(res[2]) == str else 'Failed')
print('`different` item spelling test:', 'Passed' if res[2] in [
      "university town", "non-university town"] else 'Failed')


 output should be

 Type test: Passed
`better` item type test: Passed
`p` item type test: Passed
`different` item type test: Passed
`different` item spelling test: Passed


st,p =stats.ttest_ind(university_towns['price_ratio'], non_university_towns['price_ratio'])
remember to set ttest_ind attribute nan_policy to "omit"

remember that in convert_housing_data_to_quarters() we calculate the mean for each quarter, so applying the formula above
 using convert_housing_data_to_quarters() output would produce the mean price ratio

remember that the data calculated in convert_housing_data_to_quarters() is the mean value for each quarter so the formula
above calculates the mean price ratio





Please, before you start over analysing and rewriting your code for run_ttest() make sure it returns the tuple (different,
 p, better) where

different=True or different=False depending on pvalue
p = pvalue returned from scipy.stats.ttest_ind().
better = "university town" or better = "non-university town" depending on which has a lower mean price ratio
Make sure better is spelled correctly and make sure the variables in the returned tuple have the right data types, you
can use the code below for that

res= run_ttest()
correctTypes = ', '.join(str(type(v)) for v in res) == "<class 'numpy.bool_'>, <class 'numpy.float64'>, <class 'str'>"
if correctTypes:
    print("Data types test passed")
else:
    print("Data types test failed")

and finally remember that in hdf =convert_housing_data_to_quarters() the mean value for each quarter was calculated, so
when we calculate the mean price ratio, we simply need hdf[quarter before recession] divided by hdf[recession bottom]