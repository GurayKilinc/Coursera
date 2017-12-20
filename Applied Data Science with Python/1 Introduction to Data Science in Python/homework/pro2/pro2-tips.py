print(df.info)
print(df.columns)
print(df.index)

#Pay special attention when merging two frames, if the frames have a common
#column "commonkey" use:
pd.merge(df_left,df_right,on='commonkey')

#On the other hand if the dataframes shared a common index we use:
pd.merge(df_left,df_right,left_index=True,right_index=True)

#You can also have one dataframe joined on its index and the other on its
#column. For example if df_left's index is the same as "commonkey" column in
#df_right we use:
pd.merge(df_left,df_right,left_index=True,right_on='commonkey')




