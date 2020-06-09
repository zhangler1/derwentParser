
from DerwentParser.parserPatent import parserPatent
import  pandas as pd
import time
import  os

from Region_judge.jiangsu import judgeBeToJiangSU #引入对江苏的判断

def ParserToCSV(DataDir,objective_data_filepath="output"):
    """对德文特的数据进行解析生成pandas.dataframe类型数据并转化为csv文件存储，方便后续分析.

        For each directory in the directory tree rooted at top (including top
        itself, but excluding '.' and '..'), yields a 3-tuple

            dirpath, dirnames, filenames

        dirpath is a string, the path to the directory.  dirnames is a list of
        the names of the subdirectories in dirpath (excluding '.' and '..').
        filenames is a list of the names of the non-directory files in dirpath.
        Note that the names in the lists are just names, with no path components.
        To get a full path (which begins with top) to a file or directory in
        dirpath, do os.path.join(dirpath, name).

        If optional arg 'topdown' is true or

        When topdown is true, the caller can modify the dirnames list in-place
        (e.g., via del or slice assignment),



        By default, os.walk does not follow symbolic links to subdirectories on
        systems that support them.  In order to get this functionality, set the
        optional argument 'followlinks' to true.

        Caution:

        Example:

        import os
        from os.path import join, getsize
        for root, dirs, files in os.walk('python/Lib/email'):
            print(root, "consumes", end="")
            print(sum([getsize(join(root, name)) for name in files]), end="")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories

        """
    filePathList = []
    for dirpath, dirnames, filenames in os.walk(DataDir):
        for file in filenames:
            filePathList.append(os.path.join(dirpath, file))

    patents=pd.DataFrame(columns=["Title",
                               "PatentNumber",
                               "publishDate",
                               "language",
                                "pages",
                                  "region"
                                  ])

    patNations=pd.DataFrame(columns=[
                               "PatentNumber",
                               "nationality"]
                              )
    patAEs=pd.DataFrame(columns=[
                               "PatentNumber",
                               "PatentAsignee"]
                              )
    patIPCs=pd.DataFrame(columns=[
                               "PatentNumber",
                               "IPC"]
                              )
    patAUs=pd.DataFrame(columns=[
                               "PatentNumber",
                               "author"]
                              )
    # seri={}


    for source_data_filepath in filePathList:
        print(source_data_filepath)
        with open(source_data_filepath, "r", encoding="utf-8-sig") as f:
            linesInFile = f.readlines()

        start = 0
        end = 0
        lineNumber = 0

        for line in linesInFile:
            if line.strip() == "ER":  # 意味着一个专利的终结
                end = lineNumber + 1
                patent = (parserPatent(linesInFile[start:end]))  # 将分割出的文本进行专利解析后生成专利对象加入列表
                # seri[patent.publishDate]=seri.get(patent.publishDate,0)+1
                region="World"
                if patent.nationality:
                    if patent.nationality[0] == "cn" or patent.nationality[0] == "CN":
                        region = "China"
                if patent.nationality:
                    for na in patent.nationality:
                        patNadf=pd.DataFrame(data={
                        "PatentNumber": [patent.PatentNumber],
                        "nationality": [na]})
                        patNations = patNations.append(patNadf, ignore_index=True)
                if patent.PatentAsignee:
                    for ae in patent.PatentAsignee:
                        if judgeBeToJiangSU(ae):
                            region='JiangSu'
                        patAEdf = pd.DataFrame(data={
                        "PatentNumber": [patent.PatentNumber],
                        "PatentAsignee": [ae] })
                        patAEs=patAEs.append(patAEdf,ignore_index=True)
                if patent.ipcTOP3:
                    for ipc in patent.ipcTOP3:
                        patIPCdf = pd.DataFrame(data={
                        "PatentNumber": [patent.PatentNumber],
                        "IPC": [ipc] })
                        patIPCs=patIPCs.append(patIPCdf,ignore_index=True)
                if patent.authors:
                    for au in patent.authors:
                        patAUdf = pd.DataFrame(data={
                        "PatentNumber": [patent.PatentNumber],
                        "author": [au] })
                        patAUs=patAUs.append(patAUdf,ignore_index=True)

                ptdf = pd.DataFrame(data={"Title": patent.Title,
                                        "PatentNumber": patent.PatentNumber,
                                        "publishDate": patent.publishDate,
                                        "language": patent.language,
                                        "pages":patent.pages,
                                        "region":region,
                                          "na":patent.nationality[0]
                                          },index=[0])  # 将一个patent转化成dataframe格式
                patents = patents.append(ptdf,ignore_index=True)

                start = end + 1
            lineNumber = lineNumber + 1  # 记录行数
    t=time.localtime(time.time())
    patents.to_csv(objective_data_filepath+"\\"+"NCP"+"patents"+".csv")
    patNations.to_csv(objective_data_filepath+"\\"+"NCP"+"patNations"+".csv")
    patAEs.to_csv(objective_data_filepath+"\\"+"NCP"+"patAEs"+".csv")
    patIPCs.to_csv(objective_data_filepath+"\\"+"NCP"+"patIPCs"+".csv")
    patAUs.to_csv(objective_data_filepath+"\\"+"NCP"+"patAUs"+".csv")
    # print(seri)
    # pd.Series(seri).to_csv(objective_data_filepath+"\\""years"+".csv")